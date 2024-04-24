import os
import bpy
import numpy as np
import open3d as o3d


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


def createColor(ply_file_path: str, object_name: str, color_name: str = "Col") -> bool:
    assert os.path.exists(ply_file_path)

    if object_name not in bpy.data.objects.keys():
        print("[WARN][PointCloudManager::createColor]")
        print("\t object not found in blender for object : " + object_name)
        return True

    obj = bpy.data.objects[object_name]

    point_clouds = o3d.io.read_point_cloud(ply_file_path)
    colors = np.asarray(point_clouds.colors)[:, :3]

    set_vertex_attr(obj, colors, color_name)
    print("[INFO][PointCloudManager::createColor]")
    print("\t Success for object : " + object_name)
    return True


def createColors(
    ply_file_path_list: str, object_name_list: list, color_name: str = "Col"
) -> bool:
    for ply_file_path, object_name in zip(ply_file_path_list, object_name_list):
        createColor(ply_file_path, object_name, color_name)
    return True
