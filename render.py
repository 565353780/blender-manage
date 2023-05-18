#!/usr/bin/env python
# -*- coding: utf-8 -*-

blender_manage_folder_path = 'D:/github/blender-manage'
scene_name = 'scene0231_01'

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

camera_name_list = [
    'TopView',
    'Detail-1',
    'Detail-2',
    'Detail-3',
]

import sys

sys.path.append(blender_manage_folder_path)

from blender_manage.Module.render_manager import RenderManager


def demo():
    save_folder_path = blender_manage_folder_path + '/output/' + scene_name + '/'

    render_manager = RenderManager()

    render_manager.renderAllViews(camera_name_list, collection_name_list, save_folder_path)
    return True

if __name__ == '__main__':
    demo()