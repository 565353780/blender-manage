#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

import bpy
import numpy as np

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
                        "原理化BSDF"].inputs[0].default_value = tuple(color)
                except:
                    print('[ERROR][ShadingManager::createColorMaterials]')
                    print('\t only support Chinese and English!')
                    print('\t You need to edit the name of [Principled BSDF] into your language!')
                    return False
        return True

    def bindColorMaterialsForObjects(self, color_map_name='morandi'):
        assert color_map_name in self.color_map_dict.keys()
        color_map = COLOR_MAP_DICT[color_map_name]

        for collection_name in self.collection_name_list:
            collection_object_name_list = self.getCollectionObjectNameList(collection_name)
            if collection_object_name_list is None:
                print('[WARN][ShadingManager::bindColorMaterialsForObjects]')
                print('\t getCollectionObjectNameList failed!')
                continue

            for collection_object_name in collection_object_name_list:
                object_label = getLabelFromName(collection_object_name)

                if object_label is None:
                    continue

                color_idx = object_label % len(color_map)
                color_material_name = color_map_name + '_' + str(color_idx)

                bpy.data.objects[collection_object_name].data.materials.clear()
                bpy.data.objects[collection_object_name].data.materials.append(
                    bpy.data.materials[color_material_name])
        return True

    def paintColorMapForObjects(self, color_map_name='morandi'):
        self.createColorMaterials(color_map_name)
        self.bindColorMaterialsForObjects(color_map_name)
        return True
