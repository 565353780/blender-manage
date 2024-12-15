import os
import json
import subprocess
from multiprocessing import JoinableQueue, Value, Process


def worker(
    queue: JoinableQueue,
    count: Value,
    gpu: int,
) -> None:
    while True:
        item = queue.get()
        if item is None:
            break

        shape_file_path, shape_id, render_image_num, save_image_folder_path, use_gpu, overwrite = item

        # Perform some operation on the item
        print(shape_id, gpu)
        command = (
            f"export DISPLAY=:0.{gpu} &&"
            f" {os.environ['HOME']}/Install/blender/blender --background --python render_objaverse.py --"
            f" --shape_file_path {shape_file_path}"
            f" --shape_id {shape_id}"
            f" --render_image_num {render_image_num}"
            f" --save_image_folder_path {save_image_folder_path}"
            f" --use_gpu {use_gpu}"
            f" --overwrite {overwrite}"
        )
        subprocess.run(command, shell=True)

        with count.get_lock():
            count.value += 1

        queue.task_done()


if __name__ == "__main__":
    root_list = [
        '/mnt/data/jintian/chLi/Dataset/',
        os.environ['HOME'] + '/chLi/Dataset/',
    ]

    dataset_folder_path = None
    for root in root_list:
        if os.path.exists(root):
            dataset_folder_path = root
            break

    if dataset_folder_path is None:
        print('[ERROR][render_objaverse_parallel::__main__]')
        print('\t dataset not found!')
        exit()

    json_file_path = os.environ['HOME'] + '~/github/objaverse-rendering/output/summary.json'.replace('~', '')
    render_image_num = 12
    save_image_folder_path = dataset_folder_path + 'Objaverse_82K/render/'
    use_gpu = True
    num_gpus = 1
    workers_per_gpu = 8
    overwrite = False

    if not os.path.exists(json_file_path):
        print('[ERROR][render_objaverse_parallel::__main__]')
        print('\t json not exist!')
        print('\t json_file_path:', json_file_path)
        exit()

    queue = JoinableQueue()
    count = Value("i", 0)

    # Start worker processes on each of the GPUs
    for gpu_i in range(num_gpus):
        for worker_i in range(workers_per_gpu):
            worker_i = gpu_i * workers_per_gpu + worker_i
            process = Process(
                target=worker, args=(queue, count, gpu_i)
            )
            process.daemon = True
            process.start()

    # Add items to the queue
    with open(json_file_path, 'r') as f:
        model_dict = json.load(f)

    for shape_id, shape_file_path in model_dict.items():
        queue.put([shape_file_path, shape_id, render_image_num, save_image_folder_path, use_gpu, overwrite])

    # Wait for all tasks to be completed
    queue.join()

    # Add sentinels to the queue to stop the worker processes
    for i in range(num_gpus * workers_per_gpu):
        queue.put(None)
