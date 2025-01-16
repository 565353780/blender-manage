import os

from blender_manage.Config.config import VALID_FILE_TYPES

def isFileTypeValid(file_path: str) -> bool:
    file_extension = os.path.splitext(file_path)[-1]
    return file_extension in VALID_FILE_TYPES
