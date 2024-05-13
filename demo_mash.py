import sys
sys.path.append('/Users/fufu/github/blender-manage')

import os
import bpy

from blender_manage.Module.object_manager import ObjectManager

def demo():
    datat_folder_path = '/Users/fufu/Downloads/Dataset/compare_result/metric_manifold_result_selected/ShapeNet/'
    category_id = '03001627'
    model_id_start = '1c75'

    object_manager = ObjectManager()

    category_folder_path = datat_folder_path + category_id + '/'
    model_id_list = os.listdir(category_folder_path)
    model_id_list.sort()

    for model_id in model_id_list:
        if model_id[:len(model_id_start)] != model_id_start:
            continue

        print('start load shapes from model:', model_id)
        model_folder_path = category_folder_path + model_id + '/'
        model_filename_list = os.listdir(model_folder_path)
        model_filename_list.sort()

        for model_filename in model_filename_list:
            if model_filename.split('.')[-1] not in ['ply', 'obj']:
                continue

            file_id = model_filename.split('.')[0]

            model_file_path = model_folder_path + model_filename

            object_manager.loadObjectFile(model_file_path, model_id + '_' + file_id, model_id)

        object_manager.removeCollection(model_id)
    return True

if __name__ == "__main__":
    demo()
