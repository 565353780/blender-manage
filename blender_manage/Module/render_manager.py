import os
import bpy
import numpy as np
from typing import Union

from blender_manage.Config.render import RENDER_NAME_LIST, CAMERA_NAME_LIST
from blender_manage.Method.path import createFileFolder, removeFile
from blender_manage.Module.object_manager import ObjectManager


class RenderManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def setUseBorder(self, is_use_border: bool) -> bool:
        bpy.context.scene.render.use_border = is_use_border
        bpy.context.scene.render.use_crop_to_border = is_use_border
        return True

    def setRenderResolution(self, resolution: Union[np.ndarray, list]) -> bool:
        bpy.context.scene.render.resolution_x = resolution[0]
        bpy.context.scene.render.resolution_y = resolution[1]
        return True

    def setObjectVisible(self, object_name: str, visible: bool) -> bool:
        if not self.object_manager.isObjectExist(object_name):
            return False

        bpy.data.objects[object_name].hide_set(not visible)
        return True

    def setCollectionVisible(self, collection_name: str, visible: bool) -> bool:
        if not self.object_manager.isCollectionExist(collection_name):
            return False

        for object_name in bpy.data.collections[collection_name].objects.keys():
            self.setObjectVisible(object_name, visible)
        return True

    def setObjectRenderable(self, object_name: str, renderable: bool) -> bool:
        if not self.object_manager.isObjectExist(object_name):
            return False

        bpy.data.objects[object_name].hide_render = not renderable
        return True

    def setCollectionRenderable(self, collection_name: str, renderable: bool) -> bool:
        if not self.object_manager.isCollectionExist(collection_name):
            return False

        for object_name in bpy.data.collections[collection_name].objects.keys():
            self.setObjectRenderable(object_name, renderable)
        return True

    def activateCamera(self, camera_name):
        if not self.object_manager.isObjectExist(camera_name):
            print('[ERROR][RenderManager::activateCamera]')
            print('\t camera [' + camera_name + '] not found!')
            return False

        bpy.context.scene.camera = bpy.data.objects[camera_name]
        return True

    def renderImage(self, save_image_file_path: str, overwrite: bool = False) -> bool:
        if os.path.exists(save_image_file_path):
            if overwrite:
                removeFile(save_image_file_path)
            else:
                print('[WARN][RenderManager::renderImage]')
                print('\t save image file already exist!')
                print('\t save_image_file_path:', save_image_file_path)
                return True

        createFileFolder(save_image_file_path)

        print('[INFO][RenderManager::renderImage]')
        print('\t start render image...')
        bpy.context.scene.render.film_transparent = True
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        bpy.context.scene.render.image_settings.color_depth = '16'
        bpy.context.scene.render.filepath = save_image_file_path
        bpy.context.scene.render.image_settings.compression = 0
        bpy.ops.render.render(write_still=True)
        print('\t >>> [SUCCESS]')
        return True

    def renderImages(self, camera_name_list: list, save_image_file_basepath: str, overwrite: bool = False):
        for camera_name in camera_name_list:
            if not self.activateCamera(camera_name):
                continue

            if save_image_file_basepath[-1] == '/':
                save_image_file_path = save_image_file_basepath + camera_name + '.png'
            elif save_image_file_basepath[-4:] == '.png':
                save_image_file_path = save_image_file_basepath[:-4] + '_' + camera_name + '.png'
            else:
                save_image_file_path = save_image_file_basepath + '_' + camera_name + '.png'

            self.renderImage(save_image_file_path, overwrite)
        return True
