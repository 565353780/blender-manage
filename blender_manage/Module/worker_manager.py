from time import sleep
from multiprocessing import Process, JoinableQueue, Value, Lock

from blender_manage.Method.run import runBlender


class WorkerManager(object):
    def __init__(
        self,
        workers_per_cpu: int = 1,
        workers_per_gpu: int = 1,
        gpu_id_list: list = [0],
    ) -> None:
        self.workers_per_cpu = workers_per_cpu
        self.workers_per_gpu = workers_per_gpu
        self.gpu_id_list = gpu_id_list

        self.queue = JoinableQueue()
        self.total_task_num = 0
        self.finished_task_num = Value("i", 0)
        self.lock = Lock()

        self.createWorkers()
        return

    @staticmethod
    def worker(
        queue: JoinableQueue,
        finished_task_num: Value,
        gpu_id: int,
    ) -> bool:
        while True:
            item = queue.get()
            if item is None:
                break

            python_file_path, python_args_dict, is_background, mute, skip_func = item

            if skip_func is not None:
                if skip_func(python_args_dict):
                    with finished_task_num.get_lock():
                        finished_task_num.value += 1

                    queue.task_done()

                    continue

            runBlender(
                python_file_path=python_file_path,
                python_args_dict=python_args_dict,
                is_background=is_background,
                gpu_id=gpu_id,
                mute=mute,
                with_daemon=False,
            )

            with finished_task_num.get_lock():
                finished_task_num.value += 1

            queue.task_done()
        return True

    def createWorkers(self) -> bool:
        for _ in range(self.workers_per_cpu):
            process = Process(
                target=self.worker,
                args=(self.queue, self.finished_task_num, -1),
                daemon=True,
            )
            process.start()

        for gpu_id in self.gpu_id_list:
            for _ in range(self.workers_per_gpu):
                process = Process(
                    target=self.worker,
                    args=(self.queue, self.finished_task_num, gpu_id),
                    daemon=True,
                )
                process.start()
        return True

    def addTask(
        self,
        python_file_path: str,
        python_args_dict: dict,
        is_background: bool = True,
        mute: bool = False,
        skip_func=None,
    ) -> bool:
        item = [
            python_file_path,
            python_args_dict,
            is_background,
            mute,
            skip_func,
        ]

        self.queue.put(item)
        self.total_task_num += 1
        return True

    def getFinishedTaskNum(self) -> int:
        with self.finished_task_num.get_lock():
            finished_task_num = self.finished_task_num.value
        return finished_task_num

    def getRemainedTaskNum(self) -> int:
        return self.queue.qsize()

    def waitWorkers(self) -> bool:
        while True:
            with self.finished_task_num.get_lock():
                finished_task_num = self.finished_task_num.value

            print(
                "\rFinished Tasks:",
                finished_task_num,
                "/",
                self.total_task_num,
                end="    ",
            )

            if finished_task_num == self.total_task_num:
                break
            sleep(1)
        print()

        self.queue.join()
        return True
