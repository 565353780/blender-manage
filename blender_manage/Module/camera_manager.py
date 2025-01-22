import bpy
from typing import Union

from blender_manage.Module.object_manager import ObjectManager

class CameraManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def isCameraExist(self, camera_name: str) -> bool:
        return camera_name in bpy.data.cameras.keys()

    def addCamera(self, camera_name: str, camera_type: str = 'PERSP', collection_name: Union[str, None] = None) -> bool:
        if self.isCameraExist(camera_name):
            return False

        assert camera_type in ['PERSP', 'ORTHO', 'PANO']

        camera = bpy.data.cameras.new(name=camera_name)
        camera.type = camera_type

        camera_object = bpy.data.objects.new(camera_name, camera)

        if collection_name is not None:
            self.object_manager.createNewCollection(collection_name)

            bpy.data.collections[collection_name].objects.link(camera_object)
        return True

    def setCameraData(self, camera_name: str, camera_key: str, camera_value) -> bool:
        if not self.isCameraExist(camera_name):
            return False

        camera_data = bpy.data.cameras[camera_name]

        assert hasattr(camera_data, camera_key)
        setattr(camera_data, camera_key, camera_value)
        return True

    def changeToCameraView(self, camera_name: str) -> bool:
        camera = self.object_manager.getObject(camera_name)
        if camera is None:
            print('[ERROR][CameraManager::changeToCameraView]')
            print('\t camera not found!')
            print('\t camera_name:', camera_name)
            return False

        bpy.context.view_layer.objects.active = camera
        bpy.context.scene.camera = camera
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces[0].region_3d.view_perspective = 'CAMERA'
        return True
