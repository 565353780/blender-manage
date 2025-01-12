import os

import sys
sys.path.append(os.environ['HOME'] + '/github/blender-manage')

from blender_manage.Method.uv import smart_uv_project


if __name__ == '__main__':
    obj_file_path = '/home/chli/chLi/Dataset/Objaverse_82K/manifold/000-000/0000ecca9a234cae994be239f6fec552.obj'
    save_obj_file_path = './output/uv/000-000/0000ecca9a234cae994be239f6fec552.obj'
    overwrite = False

    smart_uv_project(obj_file_path,
                     save_obj_file_path,
                     overwrite)
