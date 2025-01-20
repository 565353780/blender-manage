import os

GIT_ROOT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

if GIT_ROOT_FOLDER_PATH[-1] != '/':
    GIT_ROOT_FOLDER_PATH += '/'

import sys
sys.path.append(GIT_ROOT_FOLDER_PATH)

from blender_manage.Method.format import isFileTypeValid
from blender_manage.Method.render import renderFile


def checkFilePose():
    shape_file_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/bunny/anchor-200/pcd/400_train_pcd.ply'
    save_image_file_path = '/home/chli/chLi/Results/test/test_render.png'
    use_gpu = True
    overwrite = True

    renderFile(
        shape_file_path,
        save_image_file_path,
        use_gpu,
        overwrite,
        early_stop=True,
    )
    return True

def checkFolderPose():
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/bunny/'
    save_image_file_path = '/home/chli/chLi/Results/test/test_render.png'
    use_gpu = True
    overwrite = True

    loaded_object = False

    for root, _, files in os.walk(shape_folder_path):
        for file in files:
            if not isFileTypeValid(file):
                continue

            shape_file_path = root + '/' + file
            print('start')
            print(shape_file_path)

            renderFile(
                shape_file_path,
                save_image_file_path,
                use_gpu,
                overwrite,
                early_stop=True,
            )

            loaded_object = True
            break

        if loaded_object:
           break
    return True

if __name__ == '__main__':
    # checkFilePose()
    checkFolderPose()
