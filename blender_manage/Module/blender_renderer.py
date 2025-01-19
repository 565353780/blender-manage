import os

from blender_manage.Config.path import GIT_ROOT_FOLDER_PATH, BLENDER_BIN
from blender_manage.Method.io import getFolderTaskList, getFoldersTaskList
from blender_manage.Method.skip import skip_func_renderAroundObjaverse
from blender_manage.Module.worker_manager import WorkerManager


class BlenderRenderer(object):
    def __init__(
        self,
        workers_per_cpu: int = 8,
        workers_per_gpu: int = 8,
        is_background: bool = True,
        mute: bool = False,
        use_gpu: bool = False,
        gpu_id_list: list = [0],
    ) -> None:
        self.is_background = is_background
        self.mute = mute
        self.use_gpu = use_gpu

        self.worker_manager = WorkerManager(
            workers_per_cpu,
            workers_per_gpu,
            gpu_id_list,
        )
        return

    @staticmethod
    def isValid() -> bool:
        return BLENDER_BIN is not None

    def addTask(
        self,
        python_file_path: str,
        python_args_dict: dict,
        skip_func = None,
    ) -> bool:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::addTask]')
            print('\t git package not found!')
            print('\t GIT_ROOT_FOLDER_PATH:', GIT_ROOT_FOLDER_PATH)
            return False

        if not self.worker_manager.addTask(
            python_file_path=python_file_path,
            python_args_dict=python_args_dict,
            is_background=self.is_background,
            mute=self.mute,
            skip_func=skip_func,
        ):
            print('[ERROR][BlenderRenderer::addTask]')
            print('\t addTask failed!')
            return False

        return True

    def getFinishedTaskNum(self) -> int:
        return self.worker_manager.getFinishedTaskNum()

    def waitWorkers(self) -> bool:
        return self.worker_manager.waitWorkers()

    def renderFile(
        self,
        shape_file_path: str,
        save_image_file_path: str,
        overwrite: bool = False,
        skip_func = None,
    ) -> bool:
        python_file_path = GIT_ROOT_FOLDER_PATH + 'blender_manage/Script/render_file.py'

        python_args_dict = {
            'shape_file_path': shape_file_path,
            'save_image_file_path': save_image_file_path,
            'use_gpu': self.use_gpu,
            'overwrite': overwrite,
        }

        return self.addTask(
            python_file_path=python_file_path,
            python_args_dict=python_args_dict,
            skip_func=skip_func,
        )

    def renderAroundFile(
        self,
        shape_file_path: str,
        render_image_num: int,
        save_image_folder_path: str,
        overwrite: bool = False,
        skip_func = None,
    ) -> bool:
        python_file_path = GIT_ROOT_FOLDER_PATH + 'blender_manage/Script/render_around_file.py'

        python_args_dict = {
            'shape_file_path': shape_file_path,
            'render_image_num': render_image_num,
            'save_image_folder_path': save_image_folder_path,
            'use_gpu': self.use_gpu,
            'overwrite': overwrite,
        }

        return self.addTask(
            python_file_path=python_file_path,
            python_args_dict=python_args_dict,
            skip_func=skip_func,
        )

    def renderAroundObjaverseFile(
        self,
        shape_file_path: str,
        render_image_num: int,
        save_image_folder_path: str,
        overwrite: bool = False,
        skip_func = None,
    ) -> bool:
        python_file_path = GIT_ROOT_FOLDER_PATH + 'blender_manage/Script/render_around_objaverse_file.py'

        python_args_dict = {
            'shape_file_path': shape_file_path,
            'render_image_num': render_image_num,
            'save_image_folder_path': save_image_folder_path,
            'use_gpu': self.use_gpu,
            'overwrite': overwrite,
        }

        return self.addTask(
            python_file_path=python_file_path,
            python_args_dict=python_args_dict,
            skip_func=skip_func,
        )

    def renderFolder(
        self,
        shape_folder_path: str,
        save_image_folder_path: str,
        overwrite: bool = False,
    ) -> bool:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderFolder]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return False

        folder_task_list = getFolderTaskList(
            shape_folder_path,
            save_image_folder_path,
        )

        for folder_task in folder_task_list:
            shape_file_path, save_image_file_path = folder_task

            if not self.renderFile(
                shape_file_path,
                save_image_file_path,
                overwrite,
            ):
                print('[ERROR][BlenderRenderer::renderFolder]')
                print('\t renderFile failed!')
                continue

        return True

    def renderFolders(
        self,
        shape_folder_path: str,
        save_image_folder_path: str,
        overwrite: bool = False,
    ) -> bool:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderFolders]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return False

        folders_task_list = getFoldersTaskList(
            shape_folder_path,
            save_image_folder_path,
        )

        for folders_task in folders_task_list:
            shape_file_path, save_image_file_path = folders_task

            if not self.renderFile(
                shape_file_path,
                save_image_file_path,
                overwrite,
            ):
                print('[ERROR][BlenderRenderer::renderFolder]')
                print('\t renderFile failed!')
                continue

        return True

    def renderAroundFolder(
        self,
        shape_folder_path: str,
        render_image_num: int,
        save_image_folder_path: str,
        overwrite: bool = False,
    ) -> bool:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderAroundFolder]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return False

        folder_task_list = getFolderTaskList(
            shape_folder_path,
            save_image_folder_path,
        )

        for folder_task in folder_task_list:
            shape_file_path, save_image_folder_path = folder_task

            if not self.renderAroundFile(
                shape_file_path,
                render_image_num,
                save_image_folder_path,
                overwrite,
            ):
                print('[ERROR][BlenderRenderer::renderAroundFolder]')
                print('\t renderFile failed!')
                continue

        return True

    def renderAroundFolders(
        self,
        shape_folder_path: str,
        render_image_num: int,
        save_image_folder_path: str,
        overwrite: bool = False,
    ) -> bool:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderAroundFolders]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return False

        folders_task_list = getFoldersTaskList(
            shape_folder_path,
            save_image_folder_path,
        )

        for folders_task in folders_task_list:
            shape_file_path, save_image_folder_path = folders_task

            if not self.renderAroundFile(
                shape_file_path,
                render_image_num,
                save_image_folder_path,
                overwrite,
            ):
                print('[ERROR][BlenderRenderer::renderAroundFolders]')
                print('\t renderFile failed!')
                continue

        return True

    def renderAroundObjaverseFolder(
        self,
        shape_folder_path: str,
        render_image_num: int,
        save_image_folder_path: str,
        overwrite: bool = False,
    ) -> bool:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderAroundObjaverseFolder]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return False

        folder_task_list = getFolderTaskList(
            shape_folder_path,
            save_image_folder_path,
        )

        for folder_task in folder_task_list:
            shape_file_path, save_image_folder_path = folder_task

            if not self.renderAroundObjaverseFile(
                shape_file_path,
                render_image_num,
                save_image_folder_path,
                overwrite,
            ):
                print('[ERROR][BlenderRenderer::renderAroundFolder]')
                print('\t renderFile failed!')
                continue

        return True

    def renderAroundObjaverseFolders(
        self,
        shape_folder_path: str,
        render_image_num: int,
        save_image_folder_path: str,
        overwrite: bool = False,
    ) -> bool:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderAroundObjaverseFolders]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return False

        folders_task_list = getFoldersTaskList(
            shape_folder_path,
            save_image_folder_path,
        )

        for folders_task in folders_task_list:
            shape_file_path, save_image_folder_path = folders_task

            if not self.renderAroundObjaverseFile(
                shape_file_path,
                render_image_num,
                save_image_folder_path,
                overwrite,
                skip_func_renderAroundObjaverse,
            ):
                print('[ERROR][BlenderRenderer::renderAroundObjaverseFolders]')
                print('\t renderFile failed!')
                continue

        return True
