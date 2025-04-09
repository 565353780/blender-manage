import os
from blender_manage.Method.format import isFileTypeValid
from blender_manage.Method.path import removeFile
from blender_manage.Module.blender_manager import BlenderManager


def renderFile(
    shape_file_path: str,
    save_image_file_basepath: str,
    use_gpu: bool = False,
    overwrite: bool = False,
    early_stop: bool = False,
) -> bool:
    image_format = 'jpg'

    if not isFileTypeValid(shape_file_path):
        print('[ERROR][render::renderFile]')
        print('\t shape file not valid!')
        print('\t shape_file_path:', shape_file_path)
        return False

    object_name = shape_file_path.split('/')[-1].split('.')[0]

    if save_image_file_basepath[-1] == '/':
        save_image_file_basepath += object_name + '.' + image_format

    if os.path.exists(save_image_file_basepath):
        if not overwrite:
            return True

        removeFile(save_image_file_basepath)

    blender_manager = BlenderManager()

    blender_manager.removeAll()

    blender_manager.setRenderer(
        resolution=[1000, 1000],
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
    # blender_manager.setCollectionVisible('Lights', False)

    blender_manager.createCamera(
        name='camera_1',
        camera_type='PERSP',
        collection_name='Cameras',
        position=[-1.0581, 1.7608, 0.83803],
        rotation_euler=[65.161, 0, -148.51])
    # blender_manager.setCollectionVisible('Cameras', False)

    camera_name_list = blender_manager.object_manager.getCollectionObjectNameList('Cameras')

    collection_name = 'shapes'

    blender_manager.loadObject(
        shape_file_path=shape_file_path,
        name=object_name,
        collection_name=collection_name,
        #rotation_euler=[-94, 26, 126], # bunny
        #rotation_euler=[2, -2, -18], # XiaomiSU7
        #rotation_euler=[94, 0, 108], # RobotArm
        #rotation_euler=[90, 0, 148], # Washer
    )

    if 'LN3Diff' in shape_file_path:
        blender_manager.object_manager.setObjectRotationEuler(object_name, [180, 0, 0])

    if not blender_manager.shading_manager.useObjectColor(object_name):
        blender_manager.shading_manager.paintColorMapForObject(object_name, 'pcd')

        if 'pcd' in object_name or 'xyz' in object_name:
            blender_manager.pointcloud_manager.createColor(object_name, 0.004, 'pcd_0', object_name)

    #FIXME: to force set color for compare with other methods only
    # user can remove this line to auto load object colors
    blender_manager.shading_manager.paintColorMapForObject(object_name, 'pcd')

    # blender_manager.setCollectionVisible(collection_name, False)
    # blender_manager.setCollectionRenderable(collection_name, False)

    blender_manager.setObjectRenderable(object_name, True)

    if early_stop:
        camera_name_list = blender_manager.object_manager.getCollectionObjectNameList('Cameras')
        camera_name = camera_name_list[0]

        blender_manager.camera_manager.changeToCameraView(camera_name)

        blender_manager.object_manager.selectObject(object_name)

        blender_manager.render_manager.setRenderSettings(image_format)

        blender_manager.keepOpen()

        return True

    blender_manager.render_manager.renderImages(
        camera_name_list,
        save_image_file_basepath,
        overwrite,
        background_color=[255, 255, 255],
    )

    # blender_manager.setObjectRenderable(object_name, False)

    # blender_manager.removeCollection(collection_name)
    return True
