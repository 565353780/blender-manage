#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bpy


class ObjectManager(object):
    def __init__(self):
        return

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
            print('[ERROR][ObjectManager::getCollectionObjectList]')
            print('\t collection [' + collection_name + '] not found!')
            return None

        return bpy.data.collections[collection_name].objects

    def getCollectionObjectNameList(self, collection_name):
        collection_object_list = self.getCollectionObjectList(collection_name)

        if collection_object_list is None:
            print('[ERROR][ObjectManager::getCollectionObjectNameList]')
            print('\t getCollectionObjectList failed!')
            return None

        return collection_object_list.keys()
