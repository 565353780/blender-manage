import os
import bpy
import numpy as np
from typing import Union

from blender_manage.Method.path import createFileFolder, removeFile
from blender_manage.Module.object_manager import ObjectManager


class RenderManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def setRenderEngine(self, engine_name: str, use_gpu: bool = False) -> bool:
        assert engine_name in ['EEVEE', 'WORKBENCH', 'CYCLES']

        if engine_name == 'EEVEE':
            engine_name = 'BLENDER_EEVEE_NEXT'
        elif engine_name == 'WORKBENCH':
            engine_name = 'BLENDER_WORKBENCH'

        bpy.context.scene.render.engine = engine_name

        if engine_name == 'CYCLES':
            if use_gpu:
                bpy.context.preferences.addons['cycles'].preferences.get_devices()

                bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'

                for device in bpy.context.preferences.addons['cycles'].preferences.devices:
                    device.use = (device.type != 'CPU')

                bpy.context.scene.cycles.device = 'GPU'
            else:
                bpy.context.preferences.addons['cycles'].preferences.get_devices()

                bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'NONE'

                for device in bpy.context.preferences.addons['cycles'].preferences.devices:
                    device.use = (device.type == 'CPU')

                bpy.context.scene.cycles.device = 'CPU'
        return True

    def setUseBorder(self, is_use_border: bool) -> bool:
        bpy.context.scene.render.use_border = is_use_border
        bpy.context.scene.render.use_crop_to_border = is_use_border
        return True

    def setRenderResolution(self, resolution: Union[np.ndarray, list]) -> bool:
        bpy.context.scene.render.resolution_x = resolution[0]
        bpy.context.scene.render.resolution_y = resolution[1]
        return True

    def setBackgroundColor(self, background_color: list=[255, 255, 255]) -> bool:
        bpy.context.scene.view_settings.view_transform = 'Standard'

        bpy.context.scene.render.film_transparent = True

        # bpy.context.scene.cycles.pixel_filter_type = 'BOX'
        # bpy.context.scene.cycles.filter_width = 0.01

        bpy.context.scene.use_nodes = True
        tree = bpy.context.scene.node_tree

        for node in tree.nodes:
            tree.nodes.remove(node)

        render_layers = tree.nodes.new(type="CompositorNodeRLayers")
        composite = tree.nodes.new(type="CompositorNodeComposite")
        alpha_over = tree.nodes.new(type="CompositorNodeAlphaOver")
        white_color = tree.nodes.new(type="CompositorNodeRGB")

        alpha_over.premul = 1.0

        bg_color = np.array(background_color, dtype=float) / 255.0
        white_color.outputs[0].default_value = (bg_color[0], bg_color[1], bg_color[2], 1.0)

        tree.links.new(render_layers.outputs["Image"], alpha_over.inputs[2])
        tree.links.new(white_color.outputs[0], alpha_over.inputs[1])
        tree.links.new(alpha_over.outputs["Image"], composite.inputs["Image"])
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

    def renderImage(
        self,
        save_image_file_path: str,
        overwrite: bool = False,
        background_color: list = [255, 255, 255],
    ) -> bool:
        if save_image_file_path.split('.')[-1] == 'png':
            bpy.context.scene.render.image_settings.file_format = 'PNG'
            bpy.context.scene.render.image_settings.color_mode = 'RGBA'
            bpy.context.scene.render.image_settings.color_depth = '16'
        elif save_image_file_path.split('.')[-1] in ['jpg', 'jpeg']:
            bpy.context.scene.render.image_settings.file_format = 'JPEG'
            bpy.context.scene.render.image_settings.color_mode = 'RGB'
            bpy.context.scene.render.image_settings.color_depth = '8'
            self.setBackgroundColor(background_color)
        else:
            print('[ERROR][RenderManager::renderImage]')
            print('\t save image file type not valid!')
            print('\t save_image_file_path:', save_image_file_path)
            return False

        if os.path.exists(save_image_file_path):
            if not overwrite:
                return True

            removeFile(save_image_file_path)

        createFileFolder(save_image_file_path)

        print('[INFO][RenderManager::renderImage]')
        print('\t start render image...')
        bpy.context.scene.view_settings.view_transform = 'Standard'
        bpy.context.scene.render.film_transparent = True
        bpy.context.scene.render.filepath = save_image_file_path
        bpy.context.scene.render.image_settings.compression = 0
        bpy.context.scene.render.resolution_percentage = 100
        bpy.context.scene.render.image_settings.quality = 100
        bpy.ops.render.render(write_still=True)
        print('\t >>> [SUCCESS]')
        return True

    def renderImages(
        self,
        camera_name_list: list,
        save_image_file_basepath: str,
        overwrite: bool = False,
        background_color: list = [255, 255, 255],
    ) -> bool:
        for camera_name in camera_name_list:
            if not self.activateCamera(camera_name):
                continue

            if save_image_file_basepath[-1] == '/':
                save_image_file_path = save_image_file_basepath + camera_name + '.png'
            elif save_image_file_basepath[-4:] in ['.png', '.jpg']:
                save_image_file_path = save_image_file_basepath[:-4] + '_' + camera_name + save_image_file_basepath[-4:]
            else:
                save_image_file_path = save_image_file_basepath + '_' + camera_name + '.png'

            self.renderImage(save_image_file_path, overwrite, background_color)
        return True
