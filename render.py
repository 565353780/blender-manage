#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Module.render_manager import RenderManager

def demo():
    color_map_name = 'morandi'
    save_folder_path = 'D:/github/blender-manage/output/'

    render_manager = RenderManager()

    render_manager.renderAllViews(color_map_name=color_map_name, save_folder_path=save_folder_path)
    return True
