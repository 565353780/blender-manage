import sys
sys.path.append('/Users/fufu/github/blender-manage')

import os
import bpy
from typing import Union

from blender_manage.Module.light_manager import LightManager
from blender_manage.Module.camera_manager import CameraManager
from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
from blender_manage.Module.pointcloud_manager import PointCloudManager
from blender_manage.Module.render_manager import RenderManager

def demoRenderFolder(
    pcd_folder_path: str,
    save_image_folder_path: Union[str, None] = None,
    overwrite: bool = False) -> bool:
    if save_image_folder_path is None:
        save_image_folder_path = pcd_folder_path + 'rendered/'
        os.makedirs(save_image_folder_path, exist_ok=True)

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
    light_manager.setLightData('light_top', 'size', 5)

    light_manager.addLight('light_front', 'AREA', 'Lights')
    object_manager.setObjectPosition('light_front', [0, 2, 0])
    object_manager.setObjectRotationEuler('light_front', [-90, 0, 0])
    light_manager.setLightData('light_front', 'energy', 50)
    light_manager.setLightData('light_front', 'size', 5)

    render_manager.setCollectionVisible('Lights', False)

    camera_manager.addCamera('camera_1', 'PERSP', 'Cameras')
    object_manager.setObjectPosition('camera_1', [-2.28952, 3.48527, 1.61018])
    object_manager.setObjectRotationEuler('camera_1', [68.3606, 0, -146.509])

    render_manager.setCollectionVisible('Cameras', False)

    camera_name_list = object_manager.getCollectionObjectNameList('Cameras')

    pcd_filename_list = os.listdir(pcd_folder_path)
    pcd_filename_list.sort()

    collection_name = 'pointclouds'
    object_name_list = []
    for pcd_filename in pcd_filename_list:
        if pcd_filename.split('.')[-1] not in ['ply', 'obj']:
            continue

        object_name = pcd_filename.split('.')[0]

        pcd_file_path = pcd_folder_path + pcd_filename

        object_manager.loadObjectFile(pcd_file_path, object_name, collection_name)

        shading_manager.paintColorMapForObject(object_name, 'pcd')

        pointcloud_manager.createColor(object_name, 0.004, 'pcd_0', object_name)

        object_name_list.append(object_name)

        render_manager.setCollectionVisible(collection_name, False)
        render_manager.setCollectionRenderable(collection_name, False)

    for object_name in object_name_list:
        save_image_file_basepath = save_image_folder_path + object_name

        render_manager.setObjectRenderable(object_name, True)

        render_manager.renderImages(camera_name_list, save_image_file_basepath, overwrite)

        render_manager.setObjectRenderable(object_name, False)

    object_manager.removeCollection(collection_name)
    return True

def demoRenderFolders(root_folder_path: str, overwrite: bool = False) -> bool:
    pcd_folder_path_list = []
    for root, _, files in os.walk(root_folder_path):
        for file in files:
            if not file.endswith('.ply'):
                continue

            pcd_folder_path_list.append(root + '/')
            break

    for pcd_folder_path in pcd_folder_path_list:
        demoRenderFolder(pcd_folder_path, overwrite=overwrite)

    return True

if __name__ == "__main__":
    pcd_folder_path = '/Users/fufu/Downloads/Dataset/MashCFM/recon/20241201_18:15:47/'
    overwrite = False

    demoRenderFolders(pcd_folder_path, overwrite)
