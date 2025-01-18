import os
import bpy
import numpy as np
# import open3d as o3d


def set_vertex_attr(
    obj,
    values: np.ndarray,
    name: str,
    data_type: str = "FLOAT_VECTOR",
    domain: str = "POINT",
) -> bool:
    values = np.array(values).astype("float64")
    mesh = obj.data
    if name not in obj.data.attributes:
        mesh.attributes.new(name=name, type=data_type, domain=domain)
    v = values.flatten()
    mesh.attributes[name].data.foreach_set("vector", v)
    return True

def createColor(object_name: str, colors: np.ndarray, color_name: str = "Col") -> bool:
    if object_name not in bpy.data.objects.keys():
        print("[WARN][PointCloudManager::createColor]")
        print("\t object not found in blender for object : " + object_name)
        return True

    obj = bpy.data.objects[object_name]

    set_vertex_attr(obj, colors, color_name)
    print("[INFO][PointCloudManager::createColor]")
    print("\t Success for object : " + object_name)
    return True

def createColorFromFile(object_name: str, ply_file_path: str, color_name: str = "Col") -> bool:
    assert os.path.exists(ply_file_path)

    point_clouds = o3d.io.read_point_cloud(ply_file_path)
    colors = np.asarray(point_clouds.colors)[:, :3]

    createColor(object_name, colors, color_name)
    print("[INFO][PointCloudManager::createColorFromFile]")
    print("\t Success for object : " + object_name)
    return True


def createColors(
    object_name_list: list, ply_file_path_list: str, color_name: str = "Col"
) -> bool:
    for object_name, ply_file_path in zip(object_name_list, ply_file_path_list):
        createColor(object_name, ply_file_path, color_name)
    return True
