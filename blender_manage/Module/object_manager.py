import os
import bpy


class ObjectManager(object):
    def __init__(self):
        return

    def loadObjFile(self, obj_file_path: str) -> bool:
        if not os.path.exists(obj_file_path):
            print("[ERROR][ObjectManager::loadObjFile]")
            print("\t obj file not exist!")
            print("\t obj_file_path:", obj_file_path)
            return False

        bpy.ops.import_scene.obj(filepath=obj_file_path)
        return True

    def getObjectList(self):
        return bpy.data.objects

    def getObjectNameList(self):
        return bpy.data.objects.keys()

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

    def isObjectExist(self, object_name):
        return object_name in self.getObjectNameList()

    def isCollectionExist(self, collection_name):
        return collection_name in self.getCollectionNameList()

    def isObjectInCollection(self, object_name, collection_name):
        collection_object_name_list = self.getCollectionObjectNameList(collection_name)
        if collection_object_name_list is None:
            print("[WARN][ObjectManager::isObjectInCollection]")
            print("\t getCollectionObjectNameList failed!")
            return None

        return object_name in collection_object_name_list
