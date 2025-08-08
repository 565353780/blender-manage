import os
import subprocess
from typing import Union
from multiprocessing import Process

from blender_manage.Config.path import (
    GIT_ROOT_FOLDER_PATH,
    BLENDER_BIN_MACOS,
    BLENDER_BIN_LINUX,
    BLENDER_BIN,
)


def runCMD(command: str, mute: bool = False) -> bool:
    try:
        if mute:
            process = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                cwd=GIT_ROOT_FOLDER_PATH,
                text=True,
            )
        else:
            process = subprocess.run(
                command,
                shell=True,
                cwd=GIT_ROOT_FOLDER_PATH,
                text=True,
            )
    except:
        print("[ERROR][run::runCMD]")
        print("\t run command failed!")
        print("\t command:", command)
        return False

    return True


def getRunCMD(
    python_file_path: str,
    python_args_dict: dict = {},
    is_background: bool = True,
    gpu_id: int = 0,
) -> Union[str, None]:
    if BLENDER_BIN is None:
        print("[ERROR][run::getRunCMD]")
        print("\t blender bin not found!")
        print("\t BLENDER_BIN_MACOS:", BLENDER_BIN_MACOS)
        print("\t BLENDER_BIN_LINUX:", BLENDER_BIN_LINUX)
        return None

    if not os.path.exists(GIT_ROOT_FOLDER_PATH):
        print("[ERROR][run::getRunCMD]")
        print("\t git root folder not found!")
        print("\t GIT_ROOT_FOLDER_PATH:", GIT_ROOT_FOLDER_PATH)
        return None

    if not os.path.exists(python_file_path):
        print("[ERROR][run::getRunCMD]")
        print("\t python file not found!")
        print("\t python_file_path:", python_file_path)
        return None

    command = ""

    if gpu_id >= 0:
        command += "export CUDA_VISIBLE_DEVICES=" + str(gpu_id) + " && "
        python_args_dict["use_gpu"] = True

    command += BLENDER_BIN

    if is_background:
        command += " --background"

    command += " --python " + python_file_path

    if len(list(python_args_dict.keys())) > 0:
        command += " --"
        for key, value in python_args_dict.items():
            if isinstance(value, bool):
                if value:
                    command += " --" + key
            else:
                command += " --" + key + " " + str(value)

    return command


def runBlender(
    python_file_path: str,
    python_args_dict: dict = {},
    is_background: bool = True,
    gpu_id: int = 0,
    mute: bool = False,
    with_daemon: bool = True,
) -> Union[Process, None]:
    command = getRunCMD(
        python_file_path,
        python_args_dict,
        is_background,
        gpu_id,
    )
    if command is None:
        print("[ERROR][run::runBlender]")
        print("\t getRunCMD failed!")
        return None

    if with_daemon:
        print("[INFO][parallel_run::runBlender]")
        print("\t start run command with daemon:")
        print("\t\t", command)
        process = Process(
            target=runCMD,
            args=(
                command,
                mute,
            ),
            daemon=True,
        )

        return process

    if not mute:
        print("[INFO][parallel_run::runBlender]")
        print("\t start run command:")
        print("\t\t", command)
    if not runCMD(command, mute):
        print("[ERROR][parallel_run::runBlender]")
        print("\t runCMD failed!")
        print("\t command:", command)
        return None

    return None
