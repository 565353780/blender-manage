import os
import bpy
from typing import Union

from blender_manage.Method.pcd import createColorFromFile
from blender_manage.Module.object_manager import ObjectManager


class PointCloudManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def createColor(self, object_name: str, color: Union[np.ndarray, list]) -> bool:
        bpy.ops.node.new_geometry_nodes_modifier()
        return True

    def createColorsForMethods(
        self,
        root_folder_path: str,
        method_name_list: list,
        object_name_list: list,
        color_name: str = "Col",
    ) -> bool:
        for method_name, object_name in zip(method_name_list, object_name_list):
            ply_folder_path = root_folder_path + method_name + "/"

            ply_filename_list = os.listdir(ply_folder_path)

            max_idx = -1
            latest_ply_filename = None
            for ply_filename in ply_filename_list:
                if ".ply" not in ply_filename:
                    continue

                ply_idx = int(ply_filename.split(".ply")[0].split("_")[-1])
                if ply_idx > max_idx:
                    max_idx = ply_idx
                    latest_ply_filename = ply_filename

            if max_idx == -1:
                print("[WARN][PointCloudManager::createColorsForMethods]")
                print("\t ply not found for object : " + object_name)
                continue

            latest_ply_file_path = ply_folder_path + latest_ply_filename

            createColorFromFile(latest_ply_file_path, object_name, color_name)
        return True
