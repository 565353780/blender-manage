#!/usr/bin/env python
# -*- coding: utf-8 -*-

blender_manage_folder_path = 'D:/github/blender-manage'

import sys

sys.path.append(blender_manage_folder_path)

from blender_manage.Module.render_manager import RenderManager


def demo():
    color_map_name = 'morandi'
    save_folder_path = blender_manage_folder_path + '/output/'

    render_manager = RenderManager()

    render_manager.renderAllViews(color_map_name=color_map_name, save_folder_path=save_folder_path)
    return True