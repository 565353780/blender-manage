from blender_manage.Module.object_manager import ObjectManager

def demo():
    object_manager = ObjectManager()
    object_list = object_manager.getObjects()
    return True
