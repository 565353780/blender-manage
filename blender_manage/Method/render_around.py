import os
import bpy
import math

from blender_manage.Method.format import isFileTypeValid
from blender_manage.Module.blender_manager import BlenderManager

def renderAroundFile(
    shape_file_path: str,
    render_image_num: int,
    save_image_folder_path: str,
    use_gpu: bool = False,
    overwrite: bool = False,
) -> bool:
    camera_dist = 1.5

    if not isFileTypeValid(shape_file_path):
        print('[ERROR][render::renderAroundFile]')
        print('\t shape file not valid!')
        print('\t shape_file_path:', shape_file_path)
        return False

    blender_manager = BlenderManager()

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

    blender_manager.shading_manager.paintColorMapForObject(object_name, 'pcd')

    if 'pcd' in object_name:
        blender_manager.pointcloud_manager.createColor(object_name, 0.004, 'pcd_0', object_name)

    if 'LN3Diff' in shape_file_path:
        blender_manager.object_manager.setObjectRotationEuler(object_name, [180, 0, 0])

    blender_manager.object_manager.normalizeAllObjects()

    blender_manager.object_manager.addEmptyObject('Empty', collection_name)
    cam_constraint.target = bpy.data.objects['Empty']

    blender_manager.setCollectionVisible(collection_name, False)
    blender_manager.setCollectionRenderable(collection_name, False)

    blender_manager.setObjectRenderable(object_name, True)

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

        save_image_file_path = save_image_folder_path + object_name + f"/{i:03d}.png"
        if os.path.exists(save_image_file_path):
            continue

        blender_manager.render_manager.renderImage(save_image_file_path, overwrite)

    blender_manager.setObjectRenderable(object_name, False)

    # blender_manager.removeCollection(collection_name)
    return True
