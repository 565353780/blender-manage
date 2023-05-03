#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Module.pointcloud_manager import PointCloudManager

def demo():
    root_folder_path = 'D:/Project_chLi/Scan2CAD/Paper Writing/figure materials/all-sim-results/scene0653_00/Scanned Scene/'
    method_name_list = ['OurCAD+Guo', 'OurCAD+Schmid', 'ROCA+OurNBV', 'Ours']
    color_name = 'Col'

    pointcloud_manager = PointCloudManager()
    pointcloud_manager.createColorsForMethods(root_folder_path, method_name_list, color_name)
    return True