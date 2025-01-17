import os
import bpy
import math
from typing import Union

from blender_manage.Method.format import isFileTypeValid
from blender_manage.Module.blender_manager import BlenderManager

def renderAroundObjaverseFile(
    shape_file_path: str,
    render_image_num: int,
    save_image_folder_path: str,
    use_gpu: bool = False,
    overwrite: bool = False,
) -> bool:
    object_name = shape_file_path.split('/')[-1].split('.')[0]

    new_save_image_folder_path = save_image_folder_path + object_name + '/'

    start_tag_file_path = new_save_image_folder_path + 'start.txt'

    if os.path.exists(start_tag_file_path):
        return True

    os.makedirs(new_save_image_folder_path, exist_ok=True)
    with open(start_tag_file_path, 'w') as f:
        f.write('\n')

    camera_dist = 1.5

    if not isFileTypeValid(shape_file_path):
        print('[ERROR][render::renderAroundObjaverseFile]')
        print('\t shape file not valid!')
        print('\t shape_file_path:', shape_file_path)
        return False

    blender_manager = BlenderManager()

    blender_manager.removeAll()

    blender_manager.setRenderer(
        resolution=[518, 518],
        engine_name='CYCLES',
        use_gpu=use_gpu)

    bpy.context.scene.cycles.samples = 32
    bpy.context.scene.cycles.diffuse_bounces = 1
    bpy.context.scene.cycles.glossy_bounces = 1
    bpy.context.scene.cycles.transparent_max_bounces = 3
    bpy.context.scene.cycles.transmission_bounces = 3
    bpy.context.scene.cycles.filter_width = 0.01
    bpy.context.scene.cycles.use_denoising = True
    bpy.context.scene.render.film_transparent = True

    blender_manager.createLight(
        name='light_top',
        light_type='AREA',
        collection_name='Lights',
        position=[0, 0, 10],
        rotation_euler=[0, 0, 0],
        energy=30000,
        size=100)
    blender_manager.createLight(
        name='light_front',
        light_type='AREA',
        collection_name='Lights',
        position=[0, 10, 0],
        rotation_euler=[-90, 0, 0],
        energy=3000,
        size=100)
    blender_manager.createLight(
        name='light_back',
        light_type='AREA',
        collection_name='Lights',
        position=[0, -10, 0],
        rotation_euler=[90, 0, 0],
        energy=3000,
        size=100)
    blender_manager.createLight(
        name='light_left',
        light_type='AREA',
        collection_name='Lights',
        position=[10, 0, 0],
        rotation_euler=[0, 90, 0],
        energy=3000,
        size=100)
    blender_manager.createLight(
        name='light_right',
        light_type='AREA',
        collection_name='Lights',
        position=[-10, 0, 0],
        rotation_euler=[0, -90, 0],
        energy=3000,
        size=100)
    blender_manager.setCollectionVisible('Lights', False)

    blender_manager.createCamera(
        name='camera_1',
        camera_type='PERSP',
        collection_name='Cameras',
        position=[0, 1.2, 0],
        rotation_euler=[0, 0, 0])

    blender_manager.camera_manager.setCameraData('camera_1', 'lens', 35)
    blender_manager.camera_manager.setCameraData('camera_1', 'sensor_width', 32)

    blender_manager.setCollectionVisible('Cameras', False)

    cam = bpy.context.scene.objects['camera_1']
    cam_constraint = cam.constraints.new(type="TRACK_TO")
    cam_constraint.track_axis = "TRACK_NEGATIVE_Z"
    cam_constraint.up_axis = "UP_Y"

    collection_name = 'shapes'

    blender_manager.loadObject(shape_file_path, object_name, collection_name)
    blender_manager.object_manager.normalizeAllObjects()

    blender_manager.object_manager.addEmptyObject('Empty', collection_name)
    cam_constraint.target = bpy.data.objects['Empty']

    blender_manager.render_manager.activateCamera('camera_1')

    for i in range(render_image_num):
        theta = (i / render_image_num) * math.pi * 2
        phi = math.radians(60)
        point = [
            camera_dist * math.sin(phi) * math.cos(theta),
            camera_dist * math.sin(phi) * math.sin(theta),
            camera_dist * math.cos(phi),
        ]
        blender_manager.object_manager.setObjectPosition('camera_1', point)

        save_image_file_path = new_save_image_folder_path + f"{i:03d}.jpg"
        if os.path.exists(save_image_file_path):
            continue

        blender_manager.render_manager.renderImage(save_image_file_path, overwrite)

    # blender_manager.removeCollection(collection_name)
    return True

def renderAroundObjaverseFolder(
    shape_folder_path: str,
    render_image_num: int,
    save_image_folder_path: Union[str, None] = None,
    use_gpu: bool = False,
    overwrite: bool = False,
) -> bool:
    if save_image_folder_path is None:
        save_image_folder_path = shape_folder_path + 'rendered/'
        os.makedirs(save_image_folder_path, exist_ok=True)

    shape_filename_list = os.listdir(shape_folder_path)
    shape_filename_list.sort()

    for shape_filename in shape_filename_list:
        if not isFileTypeValid(shape_filename):
            continue

        shape_file_path = shape_folder_path + shape_filename

        if not renderAroundObjaverseFile(
            shape_file_path,
            render_image_num,
            save_image_folder_path,
            use_gpu,
            overwrite):
            print('[ERROR][render::renderAroundObjaverseFolder]')
            print('\t renderAroundFile failed!')
            continue

    return True

def renderAroundObjaverseFolders(
    root_folder_path: str,
    render_image_num: int,
    save_image_root_folder_path: Union[str, None]=None,
    use_gpu: bool = False,
    overwrite: bool = False,
) -> bool:
    if not os.path.exists(root_folder_path):
        print('[ERROR][render::renderAroundObjaverseFolders]')
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
        renderAroundObjaverseFolder(
            shape_folder_path,
            render_image_num,
            save_image_folder_path,
            use_gpu,
            overwrite)

    return True
