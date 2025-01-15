import os
from typing import Union
from subprocess import Popen

from blender_manage.Config.path import GIT_ROOT_FOLDER_PATH, BLENDER_BIN
from blender_manage.Method.run import runBlender


class BlenderRenderer(object):
    def __init__(self) -> None:
        return

    @staticmethod
    def isValid() -> bool:
        return BLENDER_BIN is not None

    @staticmethod
    def renderFile(shape_file_path: str,
                   save_image_file_path: str,
                   use_gpu: bool = False,
                   overwrite: bool = False,
                   is_background: bool = True,
                   gpu_id: int = 0,
                   ) -> Union[Popen, None]:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderFile]')
            print('\t git package not found!')
            print('\t GIT_ROOT_FOLDER_PATH:', GIT_ROOT_FOLDER_PATH)
            return None

        python_file_path = GIT_ROOT_FOLDER_PATH + 'blender_manage/Script/render_file.py'

        python_args_dict = {
            'shape_file_path': shape_file_path,
            'save_image_file_path': save_image_file_path,
            'use_gpu': use_gpu,
            'overwrite': overwrite,
        }

        process = runBlender(
            python_file_path,
            python_args_dict,
            is_background=is_background,
            gpu_id=gpu_id,
        )
        if process is None:
            print('[ERROR][BlenderRenderer::renderFile]')
            print('\t runBlender failed!')
            return None

        return process

    @staticmethod
    def renderFolder(shape_folder_path: str,
                     save_image_folder_path: str,
                     use_gpu: bool = False,
                     overwrite: bool = False,
                     is_background: bool = True,
                     gpu_id: int = 0,
                     ) -> Union[Popen, None]:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderFolder]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return None

        python_file_path = GIT_ROOT_FOLDER_PATH + 'blender_manage/Script/render_folder.py'

        python_args_dict = {
            'shape_folder_path': shape_folder_path,
            'save_image_folder_path': save_image_folder_path,
            'use_gpu': use_gpu,
            'overwrite': overwrite,
        }

        process = runBlender(
            python_file_path,
            python_args_dict,
            is_background=is_background,
            gpu_id=gpu_id,
        )
        if process is None:
            print('[ERROR][BlenderRenderer::renderFolder]')
            print('\t runBlender failed!')
            return None

        return process

    @staticmethod
    def renderFolders(shape_folder_path: str,
                      save_image_folder_path: str,
                      use_gpu: bool = False,
                      overwrite: bool = False,
                      is_background: bool = True,
                      gpu_id: int = 0,
                      ) -> Union[Popen, None]:
        if not os.path.exists(GIT_ROOT_FOLDER_PATH):
            print('[ERROR][BlenderRenderer::renderFolders]')
            print('\t git package not found!')
            print('\t git_root_folder_path:', GIT_ROOT_FOLDER_PATH)
            return None

        python_file_path = GIT_ROOT_FOLDER_PATH + 'blender_manage/Script/render_folders.py'

        python_args_dict = {
            'shape_folder_path': shape_folder_path,
            'save_image_folder_path': save_image_folder_path,
            'use_gpu': use_gpu,
            'overwrite': overwrite,
        }

        process = runBlender(
            python_file_path,
            python_args_dict,
            is_background=is_background,
            gpu_id=gpu_id,
        )
        if process is None:
            print('[ERROR][BlenderRenderer::renderFolders]')
            print('\t runBlender failed!')
            return None

        return process
