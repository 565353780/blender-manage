import os

import sys
sys.path.append(os.environ['HOME'] + '/github/blender-manage')

from blender_manage.Method.uv import smart_uv_project


if __name__ == '__main__':
    obj_file_path = '/home/chli/chLi/Dataset/Objaverse_82K/manifold/000-000/0000ecca9a234cae994be239f6fec552.obj'
    uv_map_resolution = 1024
    save_obj_file_path = '/home/chli/github/tex-gen/assets/models/00/0000ecca9a234cae994be239f6fec552/model.obj'
    overwrite = False

    smart_uv_project(obj_file_path,
                     uv_map_resolution,
                     save_obj_file_path,
                     overwrite)
