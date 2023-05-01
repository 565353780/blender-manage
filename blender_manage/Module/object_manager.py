import bpy


class ObjectManager(object):
    def __init__(self):
        return

    def getObjects(self):
        objects = bpy.data.objects
        #  for obj in objects:
        #  print(obj.name)

        collections = bpy.data.collections
        for collection in collections:
            for obj in collection.objects:
                print(collection.name, '-->', obj.name)

        object_list = []
        return object_list
