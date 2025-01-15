import os
GIT_ROOT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

import sys
sys.path.append(GIT_ROOT_FOLDER_PATH)

from time import sleep

from blender_manage.Method.render import renderFolders


if __name__ == "__main__":
    time_stamp = '20250115_19:44:22'
    shape_folder_path = '/home/chli/chLi/Results/mash-diffusion/output/sample/' + time_stamp + '/'
    save_image_folder_path = '/home/chli/chLi/Results/mash-diffusion/output/render/' + time_stamp + '/'
    use_gpu = False
    overwrite = False
    is_background = True
    gpu_id = 0
    keep_alive = True

    '''
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/adaptive/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/adaptive/'
    '''

    while True:
        renderFolders(
            shape_folder_path,
            save_image_folder_path,
            use_gpu,
            overwrite)

        if not keep_alive:
            break
        sleep(1)
