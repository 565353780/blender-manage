import os
GIT_ROOT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

if GIT_ROOT_FOLDER_PATH[-1] != '/':
    GIT_ROOT_FOLDER_PATH += '/'

import sys
sys.path.append(GIT_ROOT_FOLDER_PATH)

from blender_manage.Test.render_file import test as test_render_file

if __name__ == '__main__':
    shape_file_path = '/home/chli/chLi/Results/LN3Diff/2030000_0.obj'
    save_image_file_path = '/home/chli/chLi/Results/render_LN3Diff/2030000_0.obj'
    use_gpu = False
    overwrite = True

    test_render_file(
        shape_file_path,
        save_image_file_path,
        use_gpu,
        overwrite,
    )
