import sys
sys.path.append('/Users/fufu/github/blender-manage')

import os
from blender_manage.Module.pointcloud_manager import PointCloudManager

def demo():
    scene_name = 'scene0603_01'
    root_folder_path = 'D:/Project_chLi/Scan2CAD/Paper Writing/figure materials/all-sim-results/' + scene_name + '/'
    method_name_list = ['ours', 'wither', 'woop', 'worp']
    color_name = 'Col'

    pointcloud_manager = PointCloudManager()
    for method_name in method_name_list:
        ply_folder_path = root_folder_path + scene_name + '-' + method_name + '/scene/'

        ply_filename_list = os.listdir(ply_folder_path)

        ply_file_path = ply_folder_path + ply_filename_list[0]
        pointcloud_manager.createColor(ply_file_path, method_name, color_name)
    return True

if __name__ == '__main__':
    demo()
