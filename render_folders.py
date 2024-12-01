import os

import sys
sys.path.append(os.environ['HOME'] + '/github/blender-manage')

import bpy
from time import sleep
from typing import Union
from shutil import rmtree

from blender_manage.Module.light_manager import LightManager
from blender_manage.Module.camera_manager import CameraManager
from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
from blender_manage.Module.pointcloud_manager import PointCloudManager
from blender_manage.Module.render_manager import RenderManager

def removeFolders(root_folder_path: str, folder_name: str) -> bool:
    if not os.path.exists(root_folder_path):
        return True

    for root, dirs, _ in os.walk(root_folder_path):
        for dir in dirs:
            if dir != folder_name:
                continue

            rmtree(root + '/' + dir)

    return True

def renderFolder(
    shape_folder_path: str,
    save_image_folder_path: Union[str, None] = None,
    overwrite: bool = False) -> bool:
    if save_image_folder_path is None:
        save_image_folder_path = shape_folder_path + 'rendered/'
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
    object_manager.setObjectPosition('camera_1', [-1.0581, 1.7608, 0.83803])
    object_manager.setObjectRotationEuler('camera_1', [65.161, 0, -148.51])

    render_manager.setCollectionVisible('Cameras', False)

    camera_name_list = object_manager.getCollectionObjectNameList('Cameras')

    shape_filename_list = os.listdir(shape_folder_path)
    shape_filename_list.sort()

    collection_name = 'shapes'
    object_name_list = []
    for shape_filename in shape_filename_list:
        if shape_filename.split('.')[-1] not in ['ply', 'obj']:
            continue

        object_name = shape_filename.split('.')[0]

        shape_file_path = shape_folder_path + shape_filename

        object_manager.loadObjectFile(shape_file_path, object_name, collection_name)

        shading_manager.paintColorMapForObject(object_name, 'pcd')

        if 'pcd' in object_name:
            pointcloud_manager.createColor(object_name, 0.004, 'shape_0', object_name)

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

def renderFolders(root_folder_path: str, overwrite: bool = False) -> bool:
    shape_folder_path_list = []
    for root, _, files in os.walk(root_folder_path):
        for file in files:
            if not file.endswith('.ply'):
                continue

            shape_folder_path_list.append(root + '/')
            break

    shape_folder_path_list.sort()

    for shape_folder_path in shape_folder_path_list:
        renderFolder(shape_folder_path, overwrite=overwrite)

    return True

if __name__ == "__main__":
    shape_folder_path = '/home/chli/github/ASDF/conditional-flow-matching/output/recon/20241201_21:02:42/'
    overwrite = False

    # removeFolders(shape_folder_path, 'rendered')

    # renderFolder(shape_folder_path + 'iter-9/category/1/pcd/')

    while True:
        renderFolders(shape_folder_path, overwrite)
        sleep(10)
