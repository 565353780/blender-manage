#!/usr/bin/env python
# -*- coding: utf-8 -*-

blender_manage_folder_path = 'D:/github/blender-manage'

collection_name_list = [
    'GT',
    'ISR+M',
    'VPP-S2C+M',
    'SceneCAD+M',
    'Ours+M',
    'ISR+A',
    'VPP-S2C+A',
    'SceneCAD+A',
    'Ours',
    'ROCA+OurNBV',
    'OurCAD+Guo',
    'OurCAD+Schmid',
]

import sys

sys.path.append(blender_manage_folder_path)

from blender_manage.Module.shading_manager import ShadingManager

def demo():
    color_map_name = 'morandi'

    shading_manager = ShadingManager(collection_name_list)
    shading_manager.paintColorMapForObjects(color_map_name)
    return True

if __name__ == '__main__':
    demo()