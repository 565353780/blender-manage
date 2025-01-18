from time import sleep
from multiprocessing import Process, JoinableQueue, Value

from blender_manage.Method.run import runBlender

def worker(
    queue: JoinableQueue,
    count: Value,
    gpu_id: int,
) -> bool:
    while True:
        item = queue.get()
        if item is None:
            break

        python_file_path, python_args_dict, is_background, mute = item

        print('[INFO][parallel::worker]')
        print('\t start converting image on GPU-' + str(gpu_id))

        if not runBlender(
            python_file_path=python_file_path,
            python_args_dict=python_args_dict,
            is_background=is_background,
            gpu_id=gpu_id,
            mute=mute,
            with_daemon=False,
        ):
            print('[ERROR][parallel_run::worker]')
            print('\t runBlender failed!')

        with count.get_lock():
            count.value += 1

        queue.task_done()
    return True

def parallelRunBlender(
    python_file_path: str,
    python_args_dict: dict,
    is_background: bool = True,
    gpu_id_list: list = [0],
    workers_per_gpu: int = 8,
    mute: bool = True,
) -> bool:
    queue = JoinableQueue()
    count = Value("i", 0)

    for gpu_id in gpu_id_list:
        for _ in range(workers_per_gpu):
            process = Process(
                target=worker,
                args=(queue, count, gpu_id),
                daemon=True
            )
            process.start()

    item = [
        python_file_path,
        python_args_dict,
        is_background,
        mute,
    ]

    while True:
        if queue.empty():
            queue.put(item)
            sleep(1)

    queue.join()

    return True
