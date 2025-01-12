import os
import bpy

from blender_manage.Method.path import createFileFolder, removeFile

def smart_uv_project(obj_file_path: str,
                     save_obj_file_path: str,
                     overwrite: bool = False
                     ) -> bool:
    if not os.path.exists(obj_file_path):
        print('[ERROR][uv::smart_uv_project]')
        print('\t obj file not exist!')
        return False

    if not overwrite:
        if os.path.exists(save_obj_file_path):
            return True

        removeFile(save_obj_file_path)

    bpy.ops.wm.read_factory_settings(use_empty=True)

    try:
        bpy.ops.wm.obj_import(filepath=obj_file_path)
    except:
        print('[ERROR][uv::smart_uv_project]')
        print('\t obj_import failed!')
        print('\t obj_file_path:', obj_file_path)
        return False

    obj = bpy.context.selected_objects[0]

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.uv.smart_project(
        angle_limit=66.0,
        island_margin=0.02,
        area_weight=0.0,
        correct_aspect=True,
        scale_to_bounds=True
    )

    bpy.ops.object.mode_set(mode='OBJECT')

    createFileFolder(save_obj_file_path)

    bpy.ops.wm.obj_export(filepath=save_obj_file_path)

    return True
