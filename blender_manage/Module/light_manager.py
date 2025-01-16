import bpy
from typing import Union

from blender_manage.Config.config import VALID_LIGHT_TYPES
from blender_manage.Module.object_manager import ObjectManager

class LightManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def isLightExist(self, light_name: str) -> bool:
        return light_name in bpy.data.lights.keys()

    def addLight(self, light_name: str, light_type: str = 'AREA', collection_name: Union[str, None] = None) -> bool:
        if self.isLightExist(light_name):
            return False

        if light_type not in VALID_LIGHT_TYPES:
            print('[ERROR][LightManager::addLight]')
            print('\t light type not valid!')
            print('\t light_type:', light_type)
            print('\t VALID_LIGHT_TYPES:', VALID_LIGHT_TYPES)

        light = bpy.data.lights.new(name=light_name, type=light_type)

        light_object = bpy.data.objects.new(light_name, light)

        if collection_name is not None:
            self.object_manager.createNewCollection(collection_name)

            bpy.data.collections[collection_name].objects.link(light_object)
        return True

    def setLightData(self, light_name: str, light_key: str, light_value) -> bool:
        if not self.isLightExist(light_name):
            return False

        light_data = bpy.data.lights[light_name]

        assert hasattr(light_data, light_key)
        setattr(light_data, light_key, light_value)
        return True
