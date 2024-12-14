import bpy
from copy import deepcopy

from blender_manage.Config.collection import COLLECTION_NAME_LIST
from blender_manage.Config.color import COLOR_MAP_DICT
from blender_manage.Method.label import getLabelFromName
from blender_manage.Module.object_manager import ObjectManager


class ShadingManager(ObjectManager):
    def __init__(self,
                 collection_name_list=COLLECTION_NAME_LIST,
                 color_map_dict=COLOR_MAP_DICT):
        super().__init__()
        self.collection_name_list = collection_name_list
        self.color_map_dict = color_map_dict

        self.object_manager = ObjectManager()
        return

    def getMaterialList(self):
        return bpy.data.materials

    def getMaterialNameList(self):
        return bpy.data.materials.keys()

    def setCollectionNameList(self, collection_name_list):
        self.collection_name_list = collection_name_list
        return True

    def setColorMapDict(self, color_map_dict):
        self.color_map_dict = color_map_dict
        return True

    def createColorMaterials(self, color_map_name='morandi'):
        assert color_map_name in self.color_map_dict.keys()
        color_map = COLOR_MAP_DICT[color_map_name]

        material_name_list = deepcopy(self.getMaterialNameList())

        for color_idx, color in color_map.items():
            color_name = color_map_name + '_' + color_idx

            if color_name not in material_name_list:
                bpy.data.materials.new(color_name)

            bpy.data.materials[color_name].use_nodes = True

            # if bpy.data.materials[color_name].node_tree:
            # bpy.data.materials[color_name].node_tree.links.clear()
            # bpy.data.materials[color_name].node_tree.nodes.clear()

            try:
                bpy.data.materials[color_name].node_tree.nodes[
                    "Principled BSDF"].inputs[0].default_value = tuple(color)
            except:
                try:
                    bpy.data.materials[color_name].node_tree.nodes[
                        "原理化 BSDF"].inputs[0].default_value = tuple(color)
                except:
                    print('[ERROR][ShadingManager::createColorMaterials]')
                    print('\t only support Chinese and English!')
                    print('\t You need to edit the name of [Principled BSDF] into your language!')
                    return False
        return True

    def bindColorMaterialsForObject(self, object_name: str, color_map_name='morandi'):
        if not self.object_manager.isObjectExist(object_name):
            return False

        assert color_map_name in self.color_map_dict.keys()
        color_map = COLOR_MAP_DICT[color_map_name]

        object_label = getLabelFromName(object_name)

        if object_label is None:
            return False

        color_idx = object_label % len(color_map)
        color_material_name = color_map_name + '_' + str(color_idx)

        bpy.data.objects[object_name].data.materials.clear()
        bpy.data.objects[object_name].data.materials.append(
            bpy.data.materials[color_material_name])
        return True

    def bindColorMaterialsForObjects(self, color_map_name='morandi'):
        for collection_name in self.collection_name_list:
            collection_object_name_list = self.getCollectionObjectNameList(collection_name)
            if collection_object_name_list is None:
                print('[WARN][ShadingManager::bindColorMaterialsForObjects]')
                print('\t getCollectionObjectNameList failed!')
                continue

            for collection_object_name in collection_object_name_list:
                self.bindColorMaterialsForObject(collection_object_name, color_map)
        return True

    def paintColorMapForObject(self, object_name: str, color_map_name='morandi'):
        self.createColorMaterials(color_map_name)
        self.bindColorMaterialsForObject(object_name, color_map_name)
        return True

    def paintColorMapForObjects(self, color_map_name='morandi'):
        self.createColorMaterials(color_map_name)
        self.bindColorMaterialsForObjects(color_map_name)
        return True

    def setRenderEngine(self, engine_name: str, use_gpu: bool = False) -> bool:
        assert engine_name in ['EEVEE', 'WORKBENCH', 'CYCLES']

        if engine_name == 'EEVEE':
            engine_name = 'BLENDER_EEVEE_NEXT'
        elif engine_name == 'WORKBENCH':
            engine_name = 'BLENDER_WORKBENCH'

        bpy.context.scene.render.engine = engine_name

        if engine_name == 'CYCLES':
            if use_gpu:
                bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'

                bpy.context.preferences.addons['cycles'].preferences.get_devices()
                for device in bpy.context.preferences.addons['cycles'].preferences.devices:
                    device.use = True

                bpy.context.scene.cycles.device = 'GPU'
            else:
                bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'NONE'

                bpy.context.preferences.addons['cycles'].preferences.get_devices()
                for device in bpy.context.preferences.addons['cycles'].preferences.devices:
                    if device.type != 'CPU':
                        device.use = False
                    else:
                        device.use = True

                bpy.context.scene.cycles.device = 'CPU'

        return True
