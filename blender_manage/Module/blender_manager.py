import bpy
from typing import Union

from blender_manage.Module.light_manager import LightManager
from blender_manage.Module.camera_manager import CameraManager
from blender_manage.Module.object_manager import ObjectManager
from blender_manage.Module.shading_manager import ShadingManager
from blender_manage.Module.pointcloud_manager import PointCloudManager
from blender_manage.Module.render_manager import RenderManager


class BlenderManager(object):
    def __init__(self):
        self.light_manager = LightManager()
        self.camera_manager = CameraManager()
        self.object_manager = ObjectManager()
        self.shading_manager = ShadingManager()
        self.pointcloud_manager = PointCloudManager()
        self.render_manager = RenderManager()
        return

    def removeAll(self) -> bool:
        if not self.object_manager.removeAll():
            print('[ERROR][BlenderManager::removeAll]')
            print('\t removeAll failed!')
            return False

        return True

    def setRenderer(self,
                    resolution: list,
                    engine_name: str = 'CYCLES',
                    use_gpu: bool = False,
                    ) -> bool:
        if not self.render_manager.setRenderEngine(
            engine_name,
            use_gpu
        ):
            print('[ERROR][BlenderManager::setRenderer]')
            print('\t setRenderEngine failed!')
            return False

        self.render_manager.setUseBorder(True)
        self.render_manager.setRenderResolution(resolution)

        return True

    def setObjectRenderable(self,
                            object_name: str,
                            renderable: bool) -> bool:
        if not self.render_manager.setObjectRenderable(object_name, renderable):
            print('[ERROR][BlenderManager::setObjectRenderable]')
            print('\t setObjectRenderable failed!')
            return False

        return True

    def setCollectionVisible(self,
                             collection_name: str,
                             visible: bool) -> bool:
        if not self.render_manager.setCollectionVisible(collection_name, visible):
            print('[ERROR][BlenderManager::setCollectionVisible]')
            print('\t setCollectionVisible failed!')
            return False

        return True

    def setCollectionRenderable(self,
                                collection_name: str,
                                renderable: bool) -> bool:
        if not self.render_manager.setCollectionRenderable(collection_name, renderable):
            print('[ERROR][BlenderManager::setCollectionRenderable]')
            print('\t setCollectionRenderable failed!')
            return False

        return True

    def createLight(self,
                    name: str,
                    light_type: str = 'AREA',
                    collection_name: Union[str, None] = 'Lights',
                    position: list = [0, 0, 0],
                    rotation_euler: list = [0, 0, 0],
                    energy = 50,
                    size = 5,
                    ) -> bool:
        if not self.light_manager.addLight(name, light_type, collection_name):
            print('[ERROR][BlenderManager::createLight]')
            print('\t addLight failed!')
            return False

        if not self.object_manager.setObjectPosition(name, position):
            print('[ERROR][BlenderManager::createLight]')
            print('\t setObjectPosition failed!')
            return False

        if not self.object_manager.setObjectRotationEuler(name, rotation_euler):
            print('[ERROR][BlenderManager::createLight]')
            print('\t setObjectRotationEuler failed!')
            return False

        if not self.light_manager.setLightData(name, 'energy', energy):
            print('[ERROR][BlenderManager::createLight]')
            print('\t setLightData energy failed!')
            return False

        if not self.light_manager.setLightData(name, 'size', size):
            print('[ERROR][BlenderManager::createLight]')
            print('\t setLightData size failed!')
            return False

        return True

    def createCamera(self,
                     name: str,
                     camera_type: str = 'PERSP',
                     collection_name: Union[str, None] = 'Cameras',
                     position: list = [0, 0, 0],
                     rotation_euler: list = [0, 0, 0],
                     ) -> bool:
        if not self.camera_manager.addCamera(name, camera_type, collection_name):
            print('[ERROR][BlenderManager::createCamera]')
            print('\t addCamera failed!')
            return False

        if not self.object_manager.setObjectPosition(name, position):
            print('[ERROR][BlenderManager::createCamera]')
            print('\t setObjectPosition failed!')
            return False

        if not self.object_manager.setObjectRotationEuler(name, rotation_euler):
            print('[ERROR][BlenderManager::createCamera]')
            print('\t setObjectRotationEuler failed!')
            return False

        return True

    def loadObject(self,
                   shape_file_path: str,
                   name: str,
                   collection_name: str,
                   position: Union[list, None] = None,
                   rotation_euler: Union[list, None] = None,
                   scale: Union[list, None] = None,
                   ) -> bool:
        if not self.object_manager.loadObjectFile(shape_file_path, name, collection_name):
            print('[ERROR][BlenderManager::loadObject]')
            print('\t loadObjectFile failed!')
            return False

        if position is not None:
            if not self.object_manager.setObjectPosition(name, position):
                print('[ERROR][BlenderManager::loadObject]')
                print('\t setObjectPosition failed!')
                return False

        if rotation_euler is not None:
            if not self.object_manager.setObjectRotationEuler(name, rotation_euler):
                print('[ERROR][BlenderManager::loadObject]')
                print('\t setObjectRotationEuler failed!')
                return False

        if scale is not None:
            if not self.object_manager.setObjectScale(name, scale):
                print('[ERROR][BlenderManager::loadObject]')
                print('\t setObjectScale failed!')
                return False

        return True

    def removeCollection(self,
                         collection_name: str) -> bool:
        return self.object_manager.removeCollection(collection_name)

    def keepOpen(self) -> bool:
        def keep_open(dummy):
            pass
        bpy.app.handlers.load_post.append(keep_open)
        return True
