from blender_manage.Module.light_manager import LightManager
from blender_manage.Module.camera_manager import CameraManager
from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
from blender_manage.Module.pointcloud_manager import PointCloudManager
from blender_manage.Module.render_manager import RenderManager


def test(
    shape_file_path: str,
    save_image_file_basepath: str,
    use_gpu: bool = False,
    overwrite: bool = False) -> bool:
    if shape_file_path.split('.')[-1] not in ['ply', 'obj']:
        print('[ERROR][render::renderFile]')
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

    if 'LN3Diff' in shape_file_path:
        object_manager.setObjectRotationEuler(object_name, [180, 0, 0])

    shading_manager.paintColorMapForObject(object_name, 'pcd')

    if 'pcd' in object_name:
        pointcloud_manager.createColor(object_name, 0.004, 'pcd_0', object_name)

    render_manager.setCollectionVisible(collection_name, False)
    render_manager.setCollectionRenderable(collection_name, False)

    render_manager.setObjectRenderable(object_name, True)

    return True

    if save_image_file_basepath[-1] == '/':
        save_image_file_basepath += object_name

    render_manager.renderImages(camera_name_list, save_image_file_basepath, overwrite)

    render_manager.setObjectRenderable(object_name, False)

    object_manager.removeCollection(collection_name)
    return True
