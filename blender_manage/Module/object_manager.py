import os
import bpy
from typing import Union


class ObjectManager(object):
    def __init__(self):
        return

    def loadObjectFile(self, object_file_path: str, object_name: str, collection_name: Union[str, None]=None) -> bool:
        if not os.path.exists(object_file_path):
            print("[ERROR][ObjectManager::loadObjectFile]")
            print("\t object file not exist!")
            print("\t object_file_path:", object_file_path)
            return False

        object_file_type = object_file_path.split('.')[-1]
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

        obj = bpy.context.selected_objects[0]
        obj.name = object_name

        if collection_name is not None:
            self.createNewCollection(collection_name)

            if object_name in bpy.context.collection.objects.keys():
                bpy.context.collection.objects.unlink(obj)
            bpy.data.collections[collection_name].objects.link(obj)
        return True

    def getObjectList(self):
        return bpy.data.objects

    def getObjectNameList(self):
        return bpy.data.objects.keys()

    def createNewCollection(self, collection_name: str) -> bool:
        if self.isCollectionExist(collection_name):
            return True

        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)
        return True

    def getCollectionNameList(self):
        return bpy.data.collections.keys()

    def getCollectionList(self):
        return bpy.data.collections

    def getCollectionObjectList(self, collection_name):
        collection_name_list = self.getCollectionNameList()

        if collection_name not in collection_name_list:
            print("[ERROR][ObjectManager::getCollectionObjectList]")
            print("\t collection [" + collection_name + "] not found!")
            return None

        return bpy.data.collections[collection_name].objects

    def getCollectionObjectNameList(self, collection_name):
        collection_object_list = self.getCollectionObjectList(collection_name)

        if collection_object_list is None:
            print("[ERROR][ObjectManager::getCollectionObjectNameList]")
            print("\t getCollectionObjectList failed!")
            return None

        return collection_object_list.keys()

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
            bpy.data.objects[object_name].select = True
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
