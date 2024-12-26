import os
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

        (
            shape_file_path,
            shape_id,
            render_image_num,
            save_image_folder_path,
            use_gpu,
            overwrite,
        ) = item

        # Perform some operation on the item
        print(shape_id, gpu)
        command = (
            f"export CUDA_VISIBLE_DEVICES={gpu} &&"
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
        "/mnt/d/chLi/Dataset/",
        os.environ["HOME"] + "/chLi/Dataset/",
    ]

    dataset_folder_path = None
    for root in root_list:
        if os.path.exists(root):
            dataset_folder_path = root
            break

    if dataset_folder_path is None:
        print("[ERROR][render_objaverse_parallel::__main__]")
        print("\t dataset not found!")
        exit()

    dataset_root_folder_path = dataset_folder_path + "Objaverse_82K/glbs/"
    assert os.path.exists(dataset_root_folder_path)

    render_image_num = 12
    save_image_folder_path = dataset_folder_path + "Objaverse_82K/render/"
    use_gpu = True
    gpu_idx_list = [1, 2, 3, 4, 5, 6, 7]
    # gpu_idx_list = [0]
    workers_per_gpu = 6
    overwrite = False

    queue = JoinableQueue()
    count = Value("i", 0)

    # Start worker processes on each of the GPUs
    for gpu_i in gpu_idx_list:
        for worker_i in range(workers_per_gpu):
            worker_i = gpu_i * workers_per_gpu + worker_i
            process = Process(target=worker, args=(queue, count, gpu_i))
            process.daemon = True
            process.start()

    # Add items to the queue
    for root, _, files in os.walk(dataset_root_folder_path):
        for file in files:
            if not file.endswith(".glb"):
                continue

            rel_folder_path = os.path.relpath(root, dataset_root_folder_path)

            shape_file_path = dataset_root_folder_path + rel_folder_path + "/" + file

            shape_id = rel_folder_path + "/" + file[:-4]

            curr_save_image_folder_path = save_image_folder_path + shape_id + "/"
            if os.path.exists(curr_save_image_folder_path):
                rendered_image_file_name_list = os.listdir(curr_save_image_folder_path)

                rendered_image_num = 0
                for rendered_image_file_name in rendered_image_file_name_list:
                    if rendered_image_file_name.endswith(".png"):
                        rendered_image_num += 1

                if rendered_image_num == render_image_num:
                    continue

            queue.put(
                [
                    shape_file_path,
                    shape_id,
                    render_image_num,
                    save_image_folder_path,
                    use_gpu,
                    overwrite,
                ]
            )

    # Wait for all tasks to be completed
    queue.join()

    # Add sentinels to the queue to stop the worker processes
    for i in range(num_gpus * workers_per_gpu):
        queue.put(None)
