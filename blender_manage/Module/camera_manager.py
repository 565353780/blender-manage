import os
import bpy
import numpy as np
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

            if camera_name in bpy.data.collections['Collection'].objects.keys():
                bpy.data.collections['Collection'].objects.unlink(camera_object)
            bpy.data.collections[collection_name].objects.link(camera_object)
        return True

    def setCameraPosition(self, camera_name: str, camera_position: Union[np.ndarray, list]) -> bool:
        if not self.object_manager.isObjectExist(camera_name):
            return False

        camera_object = bpy.data.objects[camera_name]

        for i in range(3):
            camera_object.location[i] = camera_position[i]
        return True

    def setCameraRotationEuler(self, camera_name: str, camera_rotation_euler: Union[np.ndarray, list]) -> bool:
        if not self.isCameraExist(camera_name):
            return False

        camera_object = bpy.data.objects[camera_name]

        for i in range(3):
            camera_object.rotation_euler[i] = camera_rotation_euler[i] * np.pi / 180.0
        return True

    def setCameraData(self, camera_name: str, camera_key: str, camera_value) -> bool:
        if not self.isCameraExist(camera_name):
            return False

        camera_data = bpy.data.cameras[camera_name]

        assert hasattr(camera_data, camera_key)
        setattr(camera_data, camera_key, camera_value)
        return True
