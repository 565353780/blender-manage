import os

import sys
sys.path.append(os.environ['HOME'] + '/github/blender-manage')

import bpy
import math
import argparse
from typing import Union
from shutil import rmtree

from blender_manage.Module.light_manager import LightManager
from blender_manage.Module.camera_manager import CameraManager
from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
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

def renderShape(
    shape_file_path: str,
    shape_id: str,
    render_image_num: int,
    save_image_folder_path: Union[str, None] = None,
    use_gpu: bool = False,
    overwrite: bool = False) -> bool:
    camera_dist = 1.5

    if shape_file_path.split('.')[-1] not in ['ply', 'obj', 'glb', 'fbx']:
        print('[ERROR][render_objaverse::renderShape]')
        print('\t shape format not valid!')
        print('\t shape_file_path:', shape_file_path)
        return False

    if save_image_folder_path is None:
        save_image_folder_path = './output/rendered/'
        os.makedirs(save_image_folder_path, exist_ok=True)

    light_manager = LightManager()
    camera_manager = CameraManager()
    object_manager = ObjectManager()
    shading_manager = ShadingManager()
    render_manager = RenderManager()

    object_manager.removeAll()

    shading_manager.setRenderEngine('CYCLES', use_gpu)
    bpy.context.scene.cycles.samples = 32
    bpy.context.scene.cycles.diffuse_bounces = 1
    bpy.context.scene.cycles.glossy_bounces = 1
    bpy.context.scene.cycles.transparent_max_bounces = 3
    bpy.context.scene.cycles.transmission_bounces = 3
    bpy.context.scene.cycles.filter_width = 0.01
    bpy.context.scene.cycles.use_denoising = True
    bpy.context.scene.render.film_transparent = True

    render_manager.setUseBorder(True)
    render_manager.setRenderResolution([518, 518])

    light_manager.addLight('light_top', 'AREA', 'Lights')
    object_manager.setObjectPosition('light_top', [0, 0, 0.5])
    light_manager.setLightData('light_top', 'energy', 30000)
    light_manager.setLightData('light_top', 'size', 100)

    render_manager.setCollectionVisible('Lights', False)

    camera_manager.addCamera('camera_1', 'PERSP', 'Cameras')
    object_manager.setObjectPosition('camera_1', [0, 1.2, 0])
    object_manager.setObjectRotationEuler('camera_1', [0, 0, 0])

    camera_manager.setCameraData('camera_1', 'lens', 35)
    camera_manager.setCameraData('camera_1', 'sensor_width', 32)

    render_manager.setCollectionVisible('Cameras', False)

    cam = bpy.context.scene.objects['camera_1']
    cam_constraint = cam.constraints.new(type="TRACK_TO")
    cam_constraint.track_axis = "TRACK_NEGATIVE_Z"
    cam_constraint.up_axis = "UP_Y"

    collection_name = 'shapes'

    object_name = shape_id
    object_manager.loadObjectFile(shape_file_path, object_name, collection_name)
    object_manager.normalizeAllObjects()

    object_manager.addEmptyObject('Empty', collection_name)
    cam_constraint.target = bpy.data.objects['Empty']

    render_manager.setCollectionVisible(collection_name, False)
    render_manager.setCollectionRenderable(collection_name, True)

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

        save_image_file_path = save_image_folder_path + shape_id + f"/{i:03d}.png"
        if os.path.exists(save_image_file_path):
            continue

        render_manager.renderImage(save_image_file_path, overwrite)
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--shape_file_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--shape_id",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--render_image_num",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--save_image_folder_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--use_gpu",
        type=bool,
        default=False,
    )
    parser.add_argument(
        "--overwrite",
        type=bool,
        default=False,
    )

    argv = sys.argv[sys.argv.index("--") + 1 :]
    args = parser.parse_args(argv)

    renderShape(
        args.shape_file_path,
        args.shape_id,
        args.render_image_num,
        args.save_image_folder_path,
        args.use_gpu,
        args.overwrite)
