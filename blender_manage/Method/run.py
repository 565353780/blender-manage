import os
from typing import Union
from subprocess import Popen

from blender_manage.Config.path import (
    GIT_ROOT_FOLDER_PATH,
    BLENDER_BIN_MACOS,
    BLENDER_BIN_LINUX,
    BLENDER_BIN
)

def runBlender(python_file_path: str,
               python_args_dict: dict={},
               is_background: bool = True,
               gpu_id: int = 0,
               ) -> Union[Popen, None]:
    if BLENDER_BIN is None:
        print('[ERROR][run::runBlender]')
        print('\t blender bin not found!')
        print('\t BLENDER_BIN_MACOS:', BLENDER_BIN_MACOS)
        print('\t BLENDER_BIN_LINUX:', BLENDER_BIN_LINUX)
        return None

    if not os.path.exists(GIT_ROOT_FOLDER_PATH):
        print('[ERROR][run::runBlender]')
        print('\t git root folder not found!')
        print('\t GIT_ROOT_FOLDER_PATH:', GIT_ROOT_FOLDER_PATH)
        return None

    if not os.path.exists(python_file_path):
        print('[ERROR][run::runBlender]')
        print('\t python file not found!')
        print('\t python_file_path:', python_file_path)
        return None

    command = 'export CUDA_VISIBLE_DEVICES=' + str(gpu_id) + ' && '
    command += BLENDER_BIN

    if is_background:
        command += ' --background'

    command += ' --python ' + python_file_path

    if len(list(python_args_dict.keys())) > 0:
        command += ' --'
        for key, value in python_args_dict.items():
            if isinstance(value, bool):
                if value:
                    command += ' --' + key
            else:
                command += ' --' + key + ' ' + value

    with open(os.devnull, 'wb') as devnull:
        process = Popen(command,
                        stdout=devnull,
                        shell=True,
                        cwd=GIT_ROOT_FOLDER_PATH)

    return process
