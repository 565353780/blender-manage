#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bpy

from blender_manage.Config.color import COLOR_MAP_DICT
from blender_manage.Config.collection import RENDER_NAME_LIST
from blender_manage.Module.shading_manager import ShadingManager


class RenderManager(object):
    def __init__(self):
        self.shading_manager = ShadingManager()
        return

    def hideRenderCollection(self, collection_name):
        if not self.shading_manager.object_manager.isCollectionExist(collection_name):
            print('[WARN][RenderManager::hideRenderCollection]')
            print('\t collection [' + collection_name + '] not found!')
            return True

        bpy.data.collections[collection_name].hide_render = True
        return True

    def activateRenderCollection(self, collection_name):
        if not self.shading_manager.object_manager.isCollectionExist(collection_name):
            print('[WARN][RenderManager::activateRenderCollection]')
            print('\t collection [' + collection_name + '] not found!')
            return True

        bpy.data.collections[collection_name].hide_render = False
        return True

    def deactivateAllMethods(self, render_name_list=RENDER_NAME_LIST):
        for render_name in render_name_list:
            self.hideRenderCollection(render_name)
        return True

    def renderAllViews(self, render_name_list=RENDER_NAME_LIST, color_map_name='morandi', save_folder_path='D:/github/blender-manage/output/'):
        os.makedirs(save_folder_path, exist_ok=True)

        self.shading_manager.paintColorMapForObjects(color_map_name)

        for render_name in render_name_list:
            self.deactivateAllMethods(render_name_list)
            self.activateRenderCollection(render_name)

            bpy.data.scenes["Scene"].render.image_settings.file_format = 'PNG'
            bpy.data.scenes["Scene"].render.filepath = save_folder_path + render_name + '.png'
            bpy.ops.render.render(write_still=True)
        return True
