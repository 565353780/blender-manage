import os
from tqdm import tqdm
from multiprocessing import Pool

from blender_manage.Method.path import removeFile


def removeFileWithPool(inputs: list) -> bool:
    file_path, dry_run = inputs

    if dry_run:
        print('file to remove:', file_path)
    else:
        removeFile(file_path)

    return True

def clearTag(
    tag_folder_path: str,
    file_format: str,
    dry_run: bool = False,
    worker_num: int = os.cpu_count(),
) -> bool:
    inputs_list = []

    for root, _, files in os.walk(tag_folder_path):
        for file in files:

            if file.endswith(file_format) and '_tmp' not in file:
                continue

            inputs_list.append([root + '/' + file, dry_run])

    print('[INFO][tag::clearTag]')
    print('\t start remove tag files...')
    print('\t tag_folder_path:', tag_folder_path)
    try:
        with Pool(worker_num) as pool:
            results = list(tqdm(pool.imap(removeFileWithPool, inputs_list), total=len(inputs_list)))
    except RuntimeError as e:
        print('[ERROR][tag::clearTag]')
        print('\t main process caught an exception:', e)
        exit()

    return True
