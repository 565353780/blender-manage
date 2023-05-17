#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Module.pointcloud_manager import PointCloudManager

def demo():
    root_folder_path = 'D:/Project_chLi/Scan2CAD/Paper Writing/figure materials/all-sim-results/scene0603_01/'
    method_name_list = ['scan-1', 'scan-explicit', 'scan-ours']
    color_name = 'Col'

    pointcloud_manager = PointCloudManager()
    for method_name in method_name_list:
        ply_file_path = root_folder_path + method_name + '.ply'
        pointcloud_manager.createColor(ply_file_path, method_name, color_name)
    return

    pointcloud_manager.createColorsForMethods(root_folder_path, method_name_list, color_name)
    return True