import os
import bpy

from blender_manage.Method.path import createFileFolder, removeFile
from blender_manage.Module.object_manager import ObjectManager

def smart_uv_project(obj_file_path: str,
                     uv_map_resolution: int,
                     save_obj_file_path: str,
                     overwrite: bool = False
                     ) -> bool:
    if not os.path.exists(obj_file_path):
        print('[ERROR][uv::smart_uv_project]')
        print('\t obj file not exist!')
        return False

    save_mtl_file_path = save_obj_file_path[:-4] + '.mtl'
    save_uv_map_file_path = save_obj_file_path[:-4] + '.png'

    if not overwrite:
        if os.path.exists(save_obj_file_path) and \
            os.path.exists(save_mtl_file_path) and \
            os.path.exists(save_uv_map_file_path):
            return True

        removeFile(save_obj_file_path)
        removeFile(save_mtl_file_path)
        removeFile(save_uv_map_file_path)

    object_manager = ObjectManager()

    object_manager.removeAll()

    collection_name = 'shapes'
    object_name = obj_file_path.split('/')[-1].split('.')[0]

    object_manager.loadObjectFile(obj_file_path, object_name, collection_name)

    obj = object_manager.getObjectList()[object_name]

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    bpy.ops.mesh.select_all(action='SELECT')

    bpy.ops.uv.smart_project(
        angle_limit=66.0,
        island_margin=0.0,
        area_weight=0.0,
        correct_aspect=True,
        scale_to_bounds=True
    )

    bpy.ops.object.mode_set(mode='OBJECT')

    createFileFolder(save_obj_file_path)

    bpy.ops.uv.export_layout(
        filepath=save_uv_map_file_path,
        export_all=True,
        size=(uv_map_resolution, uv_map_resolution),
        opacity=0.0
    )

    bpy.ops.wm.obj_export(filepath=save_obj_file_path)

    with open(save_mtl_file_path, 'w') as f:
        f.write('newmtl material_0\n')
        f.write('Kd 1 1 1\n')
        f.write('Ka 0 0 0\n')
        f.write('Ks 0.4 0.4 0.4\n')
        f.write('Ns 10\n')
        f.write('illum 2\n')
        f.write('map_Kd ' + save_uv_map_file_path.split('/')[-1] + '\n')

    object_manager.removeCollection(collection_name)

    bpy.ops.wm.quit_blender()

    return True
