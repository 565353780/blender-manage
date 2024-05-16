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
    data_folder_path = '/Users/fufu/Downloads/Dataset/nerf/data/'
    save_image_folder_path = '/Users/fufu/Downloads/Dataset/nerf/rendered/'
    overwrite = False

    light_manager = LightManager()
    camera_manager = CameraManager()
    object_manager = ObjectManager()
    shading_manager = ShadingManager()
    pointcloud_manager = PointCloudManager()
    render_manager = RenderManager()

    object_manager.removeAll()

    shading_manager.setRenderEngine('CYCLES')

    render_manager.setUseBorder(True)
    render_manager.setRenderResolution([1080, 1080])

    light_manager.addLight('light_top', 'AREA', 'Lights')
    object_manager.setObjectPosition('light_top', [0, 0, 2])
    light_manager.setLightData('light_top', 'energy', 50)
    light_manager.setLightData('light_top', 'size', 4)

    light_manager.addLight('light_front', 'AREA', 'Lights')
    object_manager.setObjectPosition('light_front', [0, 2, 0])
    object_manager.setObjectRotationEuler('light_front', [-90, 0, 0])
    light_manager.setLightData('light_front', 'energy', 50)
    light_manager.setLightData('light_front', 'size', 4)

    render_manager.setCollectionVisible('Lights', False)

    camera_manager.addCamera('camera_1', 'PERSP', 'Cameras')

    render_manager.setCollectionVisible('Cameras', False)

    camera_name_list = object_manager.getCollectionObjectNameList('Cameras')

    nerf_name_list = os.listdir(data_folder_path)
    nerf_name_list.sort()

    for nerf_name in nerf_name_list:
        nerf_folder_path = data_folder_path + nerf_name + '/'

        if not os.path.isdir(nerf_folder_path):
            continue

        nerf_save_image_folder_path = save_image_folder_path + nerf_name + '/'

        collection_name = nerf_name

        model_filename_list = os.listdir(nerf_folder_path)
        model_filename_list.sort()

        object_name_list = []

        for model_filename in model_filename_list:
            if model_filename.split('.')[-1] not in ['ply', 'obj']:
                continue

            file_id = model_filename.split('.')[0]
            object_name = nerf_name + '_' + file_id

            model_file_path = nerf_folder_path + model_filename

            object_manager.loadObjectFile(model_file_path, object_name, collection_name)

            if nerf_name == 'chair':
                object_manager.setObjectPosition(object_name, [0, 0, 3])
                object_manager.setObjectRotationEuler(object_name, [190, 0, 210])
            elif nerf_name == 'hotdog':
                object_manager.setObjectPosition(object_name, [0.4, 0.3, 3.05])
                object_manager.setObjectRotationEuler(object_name, [204, 0, 80])

            shading_manager.paintColorMapForObject(object_name, 'mash')

            if 'pcd' in file_id:
                pointcloud_manager.createColor(object_name, 0.004, 'mash_0', object_name)

            object_name_list.append(object_name)

        render_manager.setCollectionVisible(collection_name, False)
        render_manager.setCollectionRenderable(collection_name, False)

        if nerf_name == 'chair':
            object_manager.setObjectPosition('camera_1', [-2.2022, 3.8776, 1.7664])
            object_manager.setObjectRotationEuler('camera_1', [69.159, 0, -148.51])
        elif nerf_name == 'hotdog':
            object_manager.setObjectPosition('camera_1', [-2.2476, 4.6444, 4.523])
            object_manager.setObjectRotationEuler('camera_1', [47.159, 0, -154.11])

        for object_name in object_name_list:
            save_image_file_basepath = nerf_save_image_folder_path + object_name

            render_manager.setObjectRenderable(object_name, True)

            render_manager.renderImages(camera_name_list, save_image_file_basepath, overwrite)

            render_manager.setObjectRenderable(object_name, False)

        object_manager.removeCollection(collection_name)
    return True

if __name__ == "__main__":
    demo()
