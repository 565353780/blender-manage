import os
import bpy
import numpy as np
from typing import Union

from blender_manage.Module.object_manager import ObjectManager

class LightManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def isLightExist(self, light_name: str) -> bool:
        return light_name in bpy.data.lights.keys()

    def addLight(self, light_name: str, light_type: str, collection_name: Union[str, None] = None) -> bool:
        if self.isLightExist(light_name):
            return False

        assert light_type in ['POINT', 'SUN', 'SPOT', 'AREA']

        light = bpy.data.lights.new(name=light_name, type=light_type)

        light_object = bpy.data.objects.new(light_name, light)

        if collection_name is not None:
            self.object_manager.createNewCollection(collection_name)

            if light_name in bpy.data.collections['Collection'].objects.keys():
                bpy.data.collections['Collection'].objects.unlink(light_object)
            bpy.data.collections[collection_name].objects.link(light_object)
        return True

    def setLightPosition(self, light_name: str, light_position: Union[np.ndarray, list]) -> bool:
        if not self.object_manager.isObjectExist(light_name):
            return False

        light_object = bpy.data.objects[light_name]

        for i in range(3):
            light_object.location[i] = light_position[i]
        return True

    def setLightRotationEuler(self, light_name: str, light_rotation_euler: Union[np.ndarray, list]) -> bool:
        if not self.isLightExist(light_name):
            return False

        light_object = bpy.data.objects[light_name]

        for i in range(3):
            light_object.rotation_euler[i] = light_rotation_euler[i] * np.pi / 180.0
        return True

    def setLightData(self, light_name: str, light_key: str, light_value) -> bool:
        if not self.isLightExist(light_name):
            return False

        light_data = bpy.data.lights[light_name]

        assert hasattr(light_data, light_key)
        setattr(light_data, light_key, light_value)
        return True
