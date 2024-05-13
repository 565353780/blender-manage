import sys
sys.path.append('/Users/fufu/github/blender-manage')

import os
import bpy

from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
from blender_manage.Module.pointcloud_manager import PointCloudManager

def demo():
    datat_folder_path = '/Users/fufu/Downloads/Dataset/compare_result/metric_manifold_result_selected/ShapeNet/'
    category_id = '03001627'
    model_id_start = '1c75'

    object_manager = ObjectManager()
    shading_manager = ShadingManager()
    pointcloud_manager = PointCloudManager()

    category_folder_path = datat_folder_path + category_id + '/'
    model_id_list = os.listdir(category_folder_path)
    model_id_list.sort()

    for model_id in model_id_list:
        if model_id[:len(model_id_start)] != model_id_start:
            continue

        collection_name = model_id

        model_folder_path = category_folder_path + model_id + '/'
        model_filename_list = os.listdir(model_folder_path)
        model_filename_list.sort()

        for model_filename in model_filename_list:
            if model_filename.split('.')[-1] not in ['ply', 'obj']:
                continue

            file_id = model_filename.split('.')[0]
            object_name = model_id + '_' + file_id

            model_file_path = model_folder_path + model_filename

            object_manager.loadObjectFile(model_file_path, object_name, collection_name)

            shading_manager.paintColorMapForObject(object_name, 'mash')

            if 'pcd' in file_id:
                pointcloud_manager.createColor(object_name, 0.004, 'mash_0', object_name)

            shading_manager.setRenderEngine('CYCLES')

        return True
        object_manager.removeCollection(model_id)
    return True

if __name__ == "__main__":
    demo()
