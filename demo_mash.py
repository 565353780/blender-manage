import sys
sys.path.append('/Users/fufu/github/blender-manage')

import os
import bpy

from blender_manage.Module.light_manager import LightManager
from blender_manage.Module.camera_manager import CameraManager
from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
from blender_manage.Module.pointcloud_manager import PointCloudManager
from blender_manage.Module.render_manager import RenderManager

def demo():
    datat_folder_path = '/Users/fufu/Downloads/Dataset/compare_result/metric_manifold_result_selected/ShapeNet/'
    save_image_folder_path = '/Users/fufu/Downloads/Dataset/compare_result/rendered/'
    overwrite = False

    light_manager = LightManager()
    camera_manager = CameraManager()
    object_manager = ObjectManager()
    shading_manager = ShadingManager()
    pointcloud_manager = PointCloudManager()
    render_manager = RenderManager()

    object_manager.removeAll()

    render_manager.setRenderEngine('CYCLES')

    render_manager.setUseBorder(True)
    render_manager.setRenderResolution([1080, 1080])

    light_manager.addLight('light_top', 'AREA', 'Lights')
    object_manager.setObjectPosition('light_top', [0, 0, 1])
    light_manager.setLightData('light_top', 'energy', 50)
    light_manager.setLightData('light_top', 'size', 2)

    light_manager.addLight('light_front', 'AREA', 'Lights')
    object_manager.setObjectPosition('light_front', [0, 1, 0])
    object_manager.setObjectRotationEuler('light_front', [-90, 0, 0])
    light_manager.setLightData('light_front', 'energy', 50)
    light_manager.setLightData('light_front', 'size', 2)

    render_manager.setCollectionVisible('Lights', False)

    camera_manager.addCamera('camera_1', 'PERSP', 'Cameras')
    object_manager.setObjectPosition('camera_1', [-0.86324, 1.4553, 0.6352])
    object_manager.setObjectRotationEuler('camera_1', [68.8, 0, 211.2])

    camera_manager.addCamera('camera_2', 'PERSP', 'Cameras')
    camera_manager.addCamera('camera_3', 'PERSP', 'Cameras')

    render_manager.setCollectionVisible('Cameras', False)

    camera_name_list = object_manager.getCollectionObjectNameList('Cameras')

    category_id_list = os.listdir(datat_folder_path)
    category_id_list.sort()

    for category_id in category_id_list:
        category_save_image_folder_path = save_image_folder_path + category_id + '/'

        category_folder_path = datat_folder_path + category_id + '/'
        if not os.path.exists(category_folder_path):
            continue

        model_id_list = os.listdir(category_folder_path)
        model_id_list.sort()

        for model_id in model_id_list:
            model_save_image_folder_path = category_save_image_folder_path + model_id + '/'

            collection_name = model_id

            model_folder_path = category_folder_path + model_id + '/'
            if not os.path.exists(model_folder_path):
                continue

            model_filename_list = os.listdir(model_folder_path)
            model_filename_list.sort()

            object_name_list = []

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

                object_name_list.append(object_name)

            render_manager.setCollectionVisible(collection_name, False)
            render_manager.setCollectionRenderable(collection_name, False)

            if model_id[:4] == '10c7':
                object_manager.setObjectPosition('camera_2', [-0.86324, 1.4553, 0.6352])
                object_manager.setObjectRotationEuler('camera_2', [68.8, 0, 211.2])
                object_manager.setObjectPosition('camera_3', [-0.86324, 1.4553, 0.6352])
                object_manager.setObjectRotationEuler('camera_3', [68.8, 0, 211.2])
            elif model_id[:4] == '17ac':
                object_manager.setObjectPosition('camera_2', [-0.86324, 1.4553, 0.6352])
                object_manager.setObjectRotationEuler('camera_2', [68.8, 0, 211.2])
                object_manager.setObjectPosition('camera_3', [-0.86324, 1.4553, 0.6352])
                object_manager.setObjectRotationEuler('camera_3', [68.8, 0, 211.2])

            # use return to check camera pose here
            return

            for object_name in object_name_list:
                if 'mash_pcd' in object_name:
                    continue

                save_image_file_basepath = model_save_image_folder_path + object_name

                render_manager.setObjectRenderable(object_name, True)

                render_manager.renderImages(camera_name_list, save_image_file_basepath, overwrite)

                render_manager.setObjectRenderable(object_name, False)

            object_manager.removeCollection(collection_name)
    return True

if __name__ == "__main__":
    demo()
