import os

GIT_ROOT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

if GIT_ROOT_FOLDER_PATH[-1] != '/':
    GIT_ROOT_FOLDER_PATH += '/'

import sys
sys.path.append(GIT_ROOT_FOLDER_PATH)

from blender_manage.Method.format import isFileTypeValid
from blender_manage.Method.render import renderFile

if __name__ == '__main__':
    shape_folder_path = '/home/chli/chLi/Results/mash-diffusion/output/sample/20250119_04:48:38/'
    save_image_file_path = '/home/chli/chLi/Results/test/test_render.png'
    use_gpu = True
    overwrite = True
    early_stop = True

    for root, _, files in os.walk(shape_folder_path):
        for file in files:
            if not isFileTypeValid(file):
                continue

            shape_file_path = root + '/' + file

            renderFile(
                shape_file_path,
                save_image_file_path,
                use_gpu,
                overwrite,
                early_stop,
            )

            exit()
