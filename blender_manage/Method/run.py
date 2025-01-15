import os
import subprocess

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
               ) -> bool:
    if BLENDER_BIN is None:
        print('[ERROR][run::runBlender]')
        print('\t blender bin not found!')
        print('\t BLENDER_BIN_MACOS:', BLENDER_BIN_MACOS)
        print('\t BLENDER_BIN_LINUX:', BLENDER_BIN_LINUX)
        return False

    if not os.path.exists(GIT_ROOT_FOLDER_PATH):
        print('[ERROR][run::runBlender]')
        print('\t git root folder not found!')
        print('\t GIT_ROOT_FOLDER_PATH:', GIT_ROOT_FOLDER_PATH)
        return False

    if not os.path.exists(python_file_path):
        print('[ERROR][run::runBlender]')
        print('\t python file not found!')
        print('\t python_file_path:', python_file_path)
        return False

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

    subprocess.run([command], shell=True, cwd=GIT_ROOT_FOLDER_PATH)

    return True