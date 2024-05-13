import os
import bpy
import numpy as np
from typing import Union

from blender_manage.Config.render import RENDER_NAME_LIST, CAMERA_NAME_LIST
from blender_manage.Module.object_manager import ObjectManager


class RenderManager(ObjectManager):
    def __init__(self):
        super().__init__()
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
        if not self.isObjectExist(object_name):
            return False

        bpy.data.objects[object_name].hide_set(not visible)
        return True

    def setCollectionVisible(self, collection_name: str, visible: bool) -> bool:
        if not self.isCollectionExist(collection_name):
            return False

        for object_name in bpy.data.collections[collection_name].objects.keys():
            self.setObjectVisible(object_name, visible)
        return True

    def setObjectRenderable(self, object_name: str, renderable: bool) -> bool:
        if not self.isObjectExist(object_name):
            return False

        bpy.data.objects[object_name].hide_render = not renderable
        return True

    def setCollectionVisible(self, collection_name: str, renderable: bool) -> bool:
        if not self.isCollectionExist(collection_name):
            return False

        for object_name in bpy.data.collections[collection_name].objects.keys():
            self.setObjectRenderable(object_name, renderable)
        return True

    def activateCamera(self, camera_name):
        if not self.isObjectExist(camera_name):
            print('[ERROR][RenderManager::activateCamera]')
            print('\t camera [' + camera_name + '] not found!')
            return False

        bpy.context.scene.camera = bpy.data.objects[camera_name]
        return True

    def deactivateAllMethods(self, render_name_list=RENDER_NAME_LIST):
        for render_name in render_name_list:
            self.hideRenderCollection(render_name)
        return True

    def renderCameraViews(self,
                          camera_name,
                          render_name_list=RENDER_NAME_LIST,
                          save_folder_path='D:/github/blender-manage/output/'):
        if not self.activateCamera(camera_name):
            print('[ERROR][RenderManager::renderCameraViews]')
            print('\t camera [' + camera_name + '] not found!')
            return False

        os.makedirs(save_folder_path, exist_ok=True)

        for render_name in render_name_list:
            self.deactivateAllMethods(render_name_list)
            if not self.activateRenderCollection(render_name):
                print('[WARN][RenderManager::renderAllViews]')
                print('\t activateRenderCollection [' + render_name +
                      '] failed!')
                continue

            view_name = camera_name + '_' + render_name

            save_file_path = save_folder_path + view_name + '.png'

            print('[INFO][RenderManager::renderCameraViews]')
            print('\t start render view [' + view_name + ']...')
            if os.path.exists(save_file_path):
                print('\t >>> [SKIP] found exist file!')
                continue

            bpy.data.scenes["Scene"].render.image_settings.file_format = 'PNG'
            bpy.data.scenes[
                "Scene"].render.filepath = save_folder_path + view_name + '.png'
            bpy.ops.render.render(write_still=True)
            print('\t >>> [SUCCESS]')
        return True

    def renderAllViews(self,
                       camera_name_list=CAMERA_NAME_LIST,
                       render_name_list=RENDER_NAME_LIST,
                       save_folder_path='D:/github/blender-manage/output/'):

        for camera_name in camera_name_list:
            self.renderCameraViews(camera_name, render_name_list, save_folder_path)
        return True
