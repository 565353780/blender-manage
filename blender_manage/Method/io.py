import os
from time import time
from typing import Union

from blender_manage.Method.format import isFileTypeValid


def getFolderTaskList(
    shape_folder_path: str,
    save_image_folder_path: Union[str, None] = None,
) -> list:
    folder_task_list = []

    if not os.path.exists(shape_folder_path):
        print('[ERROR][io::getFolderTaskList]')
        print('\t shape folder not exist!')
        print('\t shape_folder_path:', shape_folder_path)
        return folder_task_list

    if save_image_folder_path is None:
        save_image_folder_path = shape_folder_path + 'rendered/'
        os.makedirs(save_image_folder_path, exist_ok=True)

    shape_filename_list = os.listdir(shape_folder_path)

    for shape_filename in shape_filename_list:
        if not isFileTypeValid(shape_filename):
            continue

        shape_file_path = shape_folder_path + shape_filename

        folder_task_list.append([
            shape_file_path,
            save_image_folder_path,
        ])

    folder_task_list.sort(key=lambda x: x[0])

    return folder_task_list

def getFoldersTaskList(
    root_folder_path: str,
    save_image_root_folder_path: Union[str, None]=None,
) -> list:
    folders_task_list = []

    if not os.path.exists(root_folder_path):
        print('[ERROR][io::getFoldersTaskList]')
        print('\t root folder not exist!')
        print('\t root_folder_path:', root_folder_path)
        return folders_task_list

    last_output_time = time()

    for root, _, files in os.walk(root_folder_path):
        for file in files:
            if time() - last_output_time > 1:
                print('[INFO][io::getFoldersTaskList]')
                print('\t collected shape num:', len(folders_task_list))
                last_output_time = time()

            if not isFileTypeValid(file):
                continue

            if save_image_root_folder_path is None:
                save_image_folder_path = root + '/rendered/'
            else:
                rel_shape_folder_path = os.path.relpath(root, root_folder_path)

                save_image_folder_path = save_image_root_folder_path + rel_shape_folder_path + '/'

            shape_folder_path = root + '/'

            folders_task_list += getFolderTaskList(
                shape_folder_path,
                save_image_folder_path,
            )
            break

    folders_task_list.sort(key=lambda x: x[0])

    return folders_task_list
