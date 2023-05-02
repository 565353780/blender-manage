#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bpy

from blender_manage.Config.render import RENDER_NAME_LIST, CAMERA_NAME_LIST
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
            print('[ERROR][RenderManager::activateRenderCollection]')
            print('\t collection [' + collection_name + '] not found!')
            return False

        bpy.data.collections[collection_name].hide_render = False
        return True

    def activateCamera(self, camera_name):
        if not self.shading_manager.object_manager.isObjectExist(camera_name):
            print('[ERROR][RenderManager::activateCamera]')
            print('\t camera [' + camera_name + '] not found!')
            return False

        bpy.context.scene.camera = bpy.data.objects[camera_name]
        return True

    def deactivateAllMethods(self, render_name_list=RENDER_NAME_LIST):
        for render_name in render_name_list:
            self.hideRenderCollection(render_name)
        return True

    def renderCameraViews(self, camera_name, render_name_list=RENDER_NAME_LIST, color_map_name='morandi', save_folder_path='D:/github/blender-manage/output/'):
        if not self.activateCamera(camera_name):
            print('[ERROR][RenderManager::renderCameraViews]')
            print('\t camera [' + camera_name + '] not found!')
            return False

        os.makedirs(save_folder_path, exist_ok=True)

        self.shading_manager.paintColorMapForObjects(color_map_name)

        for render_name in render_name_list:
            self.deactivateAllMethods(render_name_list)
            if not self.activateRenderCollection(render_name):
                print('[WARN][RenderManager::renderAllViews]')
                print('\t activateRenderCollection [' + render_name + '] failed!')
                continue

            view_name = camera_name + '_' + render_name

            save_file_path = save_folder_path + view_name + '.png'

            print('[INFO][RenderManager::renderCameraViews]')
            print('\t start render view [' + view_name + ']...')
            if os.path.exists(save_file_path):
                print('\t >>> [SKIP] found exist file!')
                continue

            bpy.data.scenes["Scene"].render.image_settings.file_format = 'PNG'
            bpy.data.scenes["Scene"].render.filepath = save_folder_path + view_name + '.png'
            bpy.ops.render.render(write_still=True)
            print('\t >>> [SUCCESS]')
        return True

    def renderAllViews(self, camera_name_list=CAMERA_NAME_LIST, render_name_list=RENDER_NAME_LIST, color_map_name='morandi', save_folder_path='D:/github/blender-manage/output/'):
        for camera_name in camera_name_list:
            self.renderCameraViews(camera_name, render_name_list, color_map_name, save_folder_path)
        return True