import os
import bpy
import numpy as np
import open3d as o3d
from typing import Union

from blender_manage.Method.path import removeFile, createFileFolder
from blender_manage.Method.bound import scene_bbox


class ObjectManager(object):
    def __init__(self):
        return

    def addEmptyObject(self, object_name: str, collection_name: Union[str, None]=None) -> bool:
        obj = bpy.data.objects.new(object_name, None)

        if collection_name is None:
            bpy.context.scene.collection.objects.link(obj)
        else:
            self.createNewCollection(collection_name)

            if object_name in bpy.context.collection.objects.keys():
                bpy.context.collection.objects.unlink(obj)
            bpy.data.collections[collection_name].objects.link(obj)
        return True

    def loadObjectFile(self, object_file_path: str, object_name: str, collection_name: Union[str, None]=None) -> bool:
        if not os.path.exists(object_file_path):
            print("[ERROR][ObjectManager::loadObjectFile]")
            print("\t object file not exist!")
            print("\t object_file_path:", object_file_path)
            return False

        object_file_type = object_file_path.split('.')[-1]
        if object_file_type == 'xyz':
            tmp_obj_file_path = './output/tmp_xyz.obj'
            removeFile(tmp_obj_file_path)
            createFileFolder(tmp_obj_file_path)
            pcd = o3d.io.read_point_cloud(object_file_path)
            o3d.io.write_point_cloud(tmp_obj_file_path, pcd, write_ascii=True)

            return self.loadObjectFile(tmp_obj_file_path, object_name, collection_name)

        if object_file_type == 'ply':
            try:
                bpy.ops.wm.ply_import(filepath=object_file_path, forward_axis='NEGATIVE_Z', up_axis='Y')
            except:
                print('[ERROR][ObjectManager::loadObjectFile]')
                print('\t ply_import failed!')
                print('\t object_file_path:', object_file_path)
                return False

        elif object_file_type == 'obj':
            try:
                bpy.ops.wm.obj_import(filepath=object_file_path)
            except:
                print('[ERROR][ObjectManager::loadObjectFile]')
                print('\t obj_import failed!')
                print('\t object_file_path:', object_file_path)
                return False

        elif object_file_type == 'glb':
            try:
                bpy.ops.import_scene.gltf(filepath=object_file_path, merge_vertices=True)
            except:
                print('[ERROR][ObjectManager::loadObjectFile]')
                print('\t gltf failed!')
                print('\t object_file_path:', object_file_path)
                return False

        elif object_file_type == 'fbx':
            try:
                bpy.ops.import_scene.fbx(filepath=object_file_path)
            except:
                print('[ERROR][ObjectManager::loadObjectFile]')
                print('\t fbx failed!')
                print('\t object_file_path:', object_file_path)
                return False

        obj = bpy.context.selected_objects[0]
        obj.name = object_name

        if collection_name is not None:
            self.createNewCollection(collection_name)

            if object_name in bpy.context.collection.objects.keys():
                bpy.context.collection.objects.unlink(obj)
            bpy.data.collections[collection_name].objects.link(obj)
        return True

    def getObjects(self) -> dict:
        return bpy.data.objects

    def getObject(self, object_name: str):
        if not self.isObjectExist(object_name):
            return None

        return self.getObjects()[object_name]

    def getObjectNameList(self) -> list:
        return list(bpy.data.objects.keys())

    def createNewCollection(self, collection_name: str) -> bool:
        if self.isCollectionExist(collection_name):
            return True

        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)
        return True

    def getCollections(self) -> dict:
        return bpy.data.collections

    def getCollectionNameList(self) -> list:
        return list(bpy.data.collections.keys())

    def getCollectionObjectList(self, collection_name) -> dict:
        collection_name_list = self.getCollectionNameList()

        if collection_name not in collection_name_list:
            print("[ERROR][ObjectManager::getCollectionObjectList]")
            print("\t collection [" + collection_name + "] not found!")
            return {}

        return bpy.data.collections[collection_name].objects

    def getCollectionObjectNameList(self, collection_name) -> list:
        collection_object_list = self.getCollectionObjectList(collection_name)

        if collection_object_list is None:
            print("[ERROR][ObjectManager::getCollectionObjectNameList]")
            print("\t getCollectionObjectList failed!")
            return []

        return list(collection_object_list.keys())

    def isObjectExist(self, object_name: str) -> bool:
        return object_name in self.getObjectNameList()

    def isCollectionExist(self, collection_name: str) -> bool:
        return collection_name in self.getCollectionNameList()

    def isObjectInCollection(self, object_name, collection_name):
        collection_object_name_list = self.getCollectionObjectNameList(collection_name)
        if collection_object_name_list is None:
            print("[WARN][ObjectManager::isObjectInCollection]")
            print("\t getCollectionObjectNameList failed!")
            return None

        return object_name in collection_object_name_list

    def selectObject(self, object_name: str, additive: bool = False) -> bool:
        if not additive:
            bpy.ops.object.select_all(action='DESELECT')

        obj = self.getObject(object_name)
        if obj is None:
            print('[ERROR][ObjectManager::selectObject]')
            print('\t object not found!')
            print('\t object_name:', object_name)
            return False

        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        return True

    def setObjectPosition(self, object_name: str, object_position: Union[np.ndarray, list]) -> bool:
        if not self.isObjectExist(object_name):
            return False

        obj = bpy.data.objects[object_name]

        for i in range(3):
            obj.location[i] = object_position[i]
        return True

    def setObjectRotationEuler(self, object_name: str, object_rotation_euler: Union[np.ndarray, list]) -> bool:
        if not self.isObjectExist(object_name):
            return False

        obj = bpy.data.objects[object_name]

        for i in range(3):
            obj.rotation_euler[i] = object_rotation_euler[i] * np.pi / 180.0
        return True

    def normalizeObject(self, object_name: str) -> bool:
        if not self.isObjectExist(object_name):
            return True

        obj = bpy.data.objects[object_name]

        bbox_min, bbox_max = scene_bbox(obj)

        scale = 1.0 / max(bbox_max - bbox_min)

        obj.scale = obj.scale * scale
        bpy.context.view_layer.update()

        bbox_min, bbox_max = scene_bbox()
        offset = -(bbox_min + bbox_max) / 2.0

        obj.matrix_world.translation += offset

        return True

    def normalizeCollection(self, collection_name: str) -> bool:
        if not self.isCollectionExist(collection_name):
            return True

        collection_objects = bpy.data.collections[collection_name].objects

        bbox_min, bbox_max = scene_bbox(collection_objects)

        scale = 1.0 / max(bbox_max - bbox_min)
        for obj in collection_objects:
            obj.scale = obj.scale * scale
        bpy.context.view_layer.update()

        bbox_min, bbox_max = scene_bbox(collection_objects)
        offset = -(bbox_min + bbox_max) / 2.0

        for obj in collection_objects:
            obj.matrix_world.translation += offset

        return True

    def normalizeAllObjects(self) -> bool:
        if len(self.getObjectNameList()) == 0:
            return True

        bbox_min, bbox_max = scene_bbox()

        scale = 1.0 / max(bbox_max - bbox_min)
        for obj in bpy.context.scene.objects.values():
            if obj.parent:
                continue
            obj.scale = obj.scale * scale
        bpy.context.view_layer.update()

        bbox_min, bbox_max = scene_bbox()
        offset = -(bbox_min + bbox_max) / 2.0

        for obj in bpy.context.scene.objects.values():
            if obj.parent:
                continue
            obj.matrix_world.translation += offset

        return True

    def removeObject(self, object_name: str, clear_data: bool = True) -> bool:
        if not self.isObjectExist(object_name):
            return True

        obj = bpy.data.objects[object_name]

        bpy.data.objects.remove(obj)

        if clear_data:
            bpy.ops.outliner.orphans_purge(do_recursive=True)
        return True

    def removeCollection(self, collection_name: str, clear_data: bool = True) -> bool:
        if not self.isCollectionExist(collection_name):
            return True

        collection = bpy.data.collections[collection_name]

        for obj in collection.objects:
            self.removeObject(obj, clear_data)

        bpy.data.collections.remove(collection)

        if clear_data:
            bpy.ops.outliner.orphans_purge(do_recursive=True)
        return True

    def removeAll(self, clear_data: bool = True) -> bool:
        for collection_name in bpy.data.collections.keys():
            self.removeCollection(collection_name)

        for object_name in bpy.data.objects.keys():
            self.removeObject(object_name)
        return True
