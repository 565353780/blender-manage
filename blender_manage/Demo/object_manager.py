#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Module.object_manager import ObjectManager


def demo():
    object_manager = ObjectManager()

    collection_name_list = object_manager.getCollectionNameList()
    print('collection_name_list:')
    print(collection_name_list)

    if len(collection_name_list) > 0:
        collection_object_name_list = object_manager.getCollectionObjectNameList(
            collection_name_list[0])
        print('collection[' + collection_name_list[0] + '] object_name_list:')
        print(collection_object_name_list)
    return True
