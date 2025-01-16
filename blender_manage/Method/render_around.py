import os
import bpy
import math
from typing import Union

from blender_manage.Method.format import isFileTypeValid
from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
from blender_manage.Module.pointcloud_manager import PointCloudManager
from blender_manage.Module.render_manager import RenderManager
from blender_manage.Module.blender_manager import BlenderManager

def renderAroundFile(
    shape_file_path: str,
    render_image_num: int,
    save_image_folder_path: str,
    use_gpu: bool = False,
    overwrite: bool = False) -> bool:
    camera_dist = 1.5

    if not isFileTypeValid(shape_file_path):
        print('[ERROR][render::renderAroundFile]')
        print('\t shape file not valid!')
        print('\t shape_file_path:', shape_file_path)
        return False

    blender_manager = BlenderManager()

    object_manager = ObjectManager()
    shading_manager = ShadingManager()
    pointcloud_manager = PointCloudManager()
    render_manager = RenderManager()

    blender_manager.removeAll()

    blender_manager.setRenderer(
        resolution=[518, 518],
        engine_name='CYCLES',
        use_gpu=use_gpu)

    blender_manager.createLight(
        name='light_top',
        light_type='AREA',
        collection_name='Lights',
        position=[0, 0, 2],
        rotation_euler=[0, 0, 0],
        energy=50,
        size=5)
    blender_manager.createLight(
        name='light_front',
        light_type='AREA',
        collection_name='Lights',
        position=[0, 2, 0],
        rotation_euler=[-90, 0, 0],
        energy=50,
        size=5)
    blender_manager.setCollectionVisible('Lights', False)

    blender_manager.createCamera(
        name='camera_1',
        camera_type='PERSP',
        collection_name='Cameras',
        position=[0, 1.2, 0],
        rotation_euler=[0, 0, 0])
    blender_manager.setCollectionVisible('Cameras', False)

    cam = bpy.context.scene.objects['camera_1']
    cam_constraint = cam.constraints.new(type="TRACK_TO")
    cam_constraint.track_axis = "TRACK_NEGATIVE_Z"
    cam_constraint.up_axis = "UP_Y"

    collection_name = 'shapes'
    object_name = shape_file_path.split('/')[-1].split('.')[0]

    blender_manager.loadObject(shape_file_path, object_name, collection_name)

    shading_manager.paintColorMapForObject(object_name, 'pcd')

    if 'pcd' in object_name:
        pointcloud_manager.createColor(object_name, 0.004, 'pcd_0', object_name)

    if 'LN3Diff' in shape_file_path:
        object_manager.setObjectRotationEuler(object_name, [180, 0, 0])

    object_manager.normalizeAllObjects()

    object_manager.addEmptyObject('Empty', collection_name)
    cam_constraint.target = bpy.data.objects['Empty']

    blender_manager.setCollectionVisible(collection_name, False)
    blender_manager.setCollectionRenderable(collection_name, False)

    blender_manager.setObjectRenderable(object_name, True)

    render_manager.activateCamera('camera_1')

    for i in range(render_image_num):
        theta = (i / render_image_num) * math.pi * 2
        phi = math.radians(60)
        point = [
            camera_dist * math.sin(phi) * math.cos(theta),
            camera_dist * math.sin(phi) * math.sin(theta),
            camera_dist * math.cos(phi),
        ]
        object_manager.setObjectPosition('camera_1', point)

        save_image_file_path = save_image_folder_path + object_name + f"/{i:03d}.png"
        if os.path.exists(save_image_file_path):
            continue

        render_manager.renderImage(save_image_file_path, overwrite)

    blender_manager.setObjectRenderable(object_name, False)

    blender_manager.removeCollection(collection_name)
    return True

def renderAroundFolder(shape_folder_path: str,
                       render_image_num: int,
                       save_image_folder_path: Union[str, None] = None,
                       use_gpu: bool = False,
                       overwrite: bool = False) -> bool:
    if save_image_folder_path is None:
        save_image_folder_path = shape_folder_path + 'rendered/'
        os.makedirs(save_image_folder_path, exist_ok=True)

    shape_filename_list = os.listdir(shape_folder_path)
    shape_filename_list.sort()

    for shape_filename in shape_filename_list:
        if not isFileTypeValid(shape_filename):
            continue

        shape_file_path = shape_folder_path + shape_filename

        if not renderAroundFile(shape_file_path,
                                render_image_num,
                                save_image_folder_path,
                                use_gpu,
                                overwrite):
            print('[ERROR][render::renderAroundFolder]')
            print('\t renderAroundFile failed!')
            continue

    return True

def renderAroundFolders(root_folder_path: str,
                        render_image_num: int,
                        save_image_root_folder_path: Union[str, None]=None,
                        use_gpu: bool = False,
                        overwrite: bool = False) -> bool:
    if not os.path.exists(root_folder_path):
        print('[ERROR][render::renderAroundFolders]')
        print('\t root folder not exist!')
        print('\t root_folder_path:', root_folder_path)
        return False

    shape_folder_path_list = []
    save_image_folder_path_list = []
    for root, _, files in os.walk(root_folder_path):
        for file in files:
            if not isFileTypeValid(file):
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
        renderAroundFolder(shape_folder_path,
                           render_image_num,
                           save_image_folder_path,
                           use_gpu,
                           overwrite)

    return True
