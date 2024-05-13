import os
import bpy

from blender_manage.Method.pcd import createColorFromFile
from blender_manage.Module.object_manager import ObjectManager


class PointCloudManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def createColor(self, object_name: str, point_radius: float, material_name: str, geometry_node_name: str) -> bool:
        if not self.object_manager.isObjectExist(object_name):
            return False

        obj = bpy.data.objects[object_name]

        if geometry_node_name not in obj.modifiers.keys():
            geometry_node = obj.modifiers.new(geometry_node_name, 'NODES')
            bpy.ops.node.new_geometry_node_group_assign()

            try:
                input = geometry_node.node_group.nodes['Group Input']
            except:
                try:
                    input = geometry_node.node_group.nodes['组输入']
                except:
                    print('[ERROR][PointCloudManager::createColor]')
                    print('\t only support Chinese and English!')
                    print('\t You need to edit the name of [Group Input] into your language!')
                    return False

            input.location = (0,0)

            try:
                output = geometry_node.node_group.nodes['Group Output']
            except:
                try:
                    output = geometry_node.node_group.nodes['组输出']
                except:
                    print('[ERROR][PointCloudManager::createColor]')
                    print('\t only support Chinese and English!')
                    print('\t You need to edit the name of [Group Output] into your language!')
                    return False

            output.location = (1000,0)

            mesh_to_points = geometry_node.node_group.nodes.new('GeometryNodeMeshToPoints')
            mesh_to_points.location = (300, 0)
            mesh_to_points.inputs[3].default_value = point_radius

            material_set = geometry_node.node_group.nodes.new('GeometryNodeSetMaterial')
            material_set.location = (600, 0)
            material_set.inputs[2].default_value = bpy.data.materials[material_name]

            geometry_node.node_group.links.new(input.outputs[0], mesh_to_points.inputs[0])
            geometry_node.node_group.links.new(mesh_to_points.outputs[0], material_set.inputs[0])
            geometry_node.node_group.links.new(material_set.outputs[0], output.inputs[0])
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
