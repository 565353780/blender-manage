import os

import sys
sys.path.append(os.environ['HOME'] + '/github/blender-manage')

import bpy
from time import sleep
from typing import Union
from shutil import rmtree

from blender_manage.Method.path import removeFile
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

def renderFile(
    shape_file_path: str,
    save_image_file_basepath: str,
    use_gpu: bool = False,
    overwrite: bool = False) -> bool:
    if shape_file_path.split('.')[-1] not in ['ply', 'obj']:
        print('[ERROR][render_folders::renderFile]')
        print('\t shape file not valid!')
        print('\t shape_file_path:', shape_file_path)
        return False

    light_manager = LightManager()
    camera_manager = CameraManager()
    object_manager = ObjectManager()
    shading_manager = ShadingManager()
    pointcloud_manager = PointCloudManager()
    render_manager = RenderManager()

    object_manager.removeAll()

    shading_manager.setRenderEngine('CYCLES', use_gpu)

    render_manager.setUseBorder(True)
    render_manager.setRenderResolution([518, 518])

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

    collection_name = 'shapes'
    object_name = shape_file_path.split('/')[-1].split('.')[0]

    object_manager.loadObjectFile(shape_file_path, object_name, collection_name)

    shading_manager.paintColorMapForObject(object_name, 'pcd')

    if 'pcd' in object_name:
        pointcloud_manager.createColor(object_name, 0.004, 'pcd_0', object_name)

    render_manager.setCollectionVisible(collection_name, False)
    render_manager.setCollectionRenderable(collection_name, False)

    render_manager.setObjectRenderable(object_name, True)

    if save_image_file_basepath[-1] == '/':
        save_image_file_basepath += object_name

    render_manager.renderImages(camera_name_list, save_image_file_basepath, overwrite)

    render_manager.setObjectRenderable(object_name, False)

    object_manager.removeCollection(collection_name)
    return True

def renderFolder(
    shape_folder_path: str,
    save_image_folder_path: Union[str, None] = None,
    use_gpu: bool = False,
    overwrite: bool = False) -> bool:
    if save_image_folder_path is None:
        save_image_folder_path = shape_folder_path + 'rendered/'
        os.makedirs(save_image_folder_path, exist_ok=True)

    shape_filename_list = os.listdir(shape_folder_path)
    shape_filename_list.sort()

    for shape_filename in shape_filename_list:
        if shape_filename.split('.')[-1] not in ['ply', 'obj']:
            continue

        shape_file_path = shape_folder_path + shape_filename

        if not renderFile(shape_file_path, save_image_folder_path, use_gpu, overwrite):
            print('[ERROR][render_folders::renderFolder]')
            print('\t renderFile failed!')
            continue

    return True

def renderFolders(
        root_folder_path: str,
        save_image_root_folder_path: Union[str, None]=None,
        use_gpu: bool = False,
        overwrite: bool = False) -> bool:
    if not os.path.exists(root_folder_path):
        print('[ERROR][render_folders::renderFolders]')
        print('\t root folder not exist!')
        print('\t root_folder_path:', root_folder_path)
        return False

    shape_folder_path_list = []
    save_image_folder_path_list = []
    for root, _, files in os.walk(root_folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[-1]
            if file_extension not in ['.ply']:
                continue

            if save_image_root_folder_path is None:
                save_image_folder_path = root + '/rendered/'
            else:
                rel_shape_folder_path = os.path.relpath(root, root_folder_path)

                save_image_folder_path = save_image_root_folder_path + rel_shape_folder_path + '/'

            shape_folder_path_list.append(root + '/')
            save_image_folder_path_list.append(save_image_folder_path)
            break

    for shape_folder_path, save_image_folder_path in zip(shape_folder_path_list, save_image_folder_path_list):
        renderFolder(shape_folder_path, save_image_folder_path, use_gpu, overwrite)

    return True

if __name__ == "__main__":
    timestamp = '20241218_15:08:27'
    root_folder_path = os.environ['HOME'] + '/github/ASDF/conditional-flow-matching/output/'
    shape_folder_path = root_folder_path + 'recon_smooth/' + timestamp + '/'
    save_image_folder_path = root_folder_path + 'render_recon_smooth/' + timestamp + '/'
    use_gpu = False
    overwrite = False

    shape_folder_path = '/home/chli/github/ASDF/ma-sh/output/fit/'
    save_image_folder_path = '/home/chli/github/ASDF/ma-sh/output/fit_render/'

    renderFolders(shape_folder_path, save_image_folder_path, use_gpu, overwrite)
    exit()

    sample_t_num = 2

    # removeFolders(shape_folder_path, 'rendered')

    while True:
        for i in range(sample_t_num - 1, -1, -1):
            shape_folder_path = root_folder_path + 'sample/' + timestamp + '/iter_' + str(i) + '/'
            save_image_folder_path = root_folder_path + 'render_sample/' + timestamp + '/iter_' + str(i) + '/'
            renderFolders(shape_folder_path, save_image_folder_path, use_gpu, overwrite)

        shape_folder_path = root_folder_path + 'recon/' + timestamp + '/iter_' + str(sample_t_num - 1) + '/'
        save_image_folder_path = root_folder_path + 'render_recon/' + timestamp + '/iter_' + str(sample_t_num - 1) + '/'
        renderFolders(shape_folder_path, save_image_folder_path, use_gpu, overwrite)

        shape_folder_path = root_folder_path + 'recon_smooth/' + timestamp + '/iter_' + str(sample_t_num - 1) + '/'
        save_image_folder_path = root_folder_path + 'render_recon_smooth/' + timestamp + '/iter_' + str(sample_t_num - 1) + '/'
        renderFolders(shape_folder_path, save_image_folder_path, use_gpu, overwrite)

        sleep(10)
