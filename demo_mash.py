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
    category_id = '03001627'
    model_id_start = '1c75'

    light_manager = LightManager()
    camera_manager = CameraManager()
    object_manager = ObjectManager()
    shading_manager = ShadingManager()
    pointcloud_manager = PointCloudManager()
    render_manager = RenderManager()

    object_manager.removeObject('Cube')
    object_manager.removeObject('Camera')
    object_manager.removeObject('Light')

    shading_manager.setRenderEngine('CYCLES')

    render_manager.setUseBorder(True)
    render_manager.setRenderResolution([1080, 1080])

    light_manager.addLight('light_top', 'AREA', 'Lights')
    light_manager.setLightPosition('light_top', [0, 0, 1])
    light_manager.setLightData('light_top', 'energy', 50)
    light_manager.setLightData('light_top', 'size', 2)

    render_manager.setObjectVisible('light_top', False)

    light_manager.addLight('light_front', 'AREA', 'Lights')
    light_manager.setLightPosition('light_front', [0, 1, 0])
    light_manager.setLightRotationEuler('light_front', [-90, 0, 0])
    light_manager.setLightData('light_front', 'energy', 50)
    light_manager.setLightData('light_front', 'size', 2)

    render_manager.setObjectVisible('light_front', False)

    camera_manager.addCamera('camera_1', 'PERSP', 'Cameras')
    camera_manager.setCameraPosition('camera_1', [-0.86324, 1.4553, 0.6352])
    camera_manager.setCameraRotationEuler('camera_1', [68.8, 0, 211.2])

    render_manager.setObjectVisible('camera_top', False)

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

            render_manager.setObjectVisible(object_name, False)
            render_manager.setObjectRenderable(object_name, False)

        return True
        object_manager.removeCollection(model_id)
    return True

if __name__ == "__main__":
    demo()
