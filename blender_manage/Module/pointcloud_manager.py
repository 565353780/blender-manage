#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import bpy
import numpy as np
import open3d as o3d

from blender_manage.Module.object_manager import ObjectManager

def set_vertex_attr(obj, values, name, data_type='FLOAT_VECTOR', domain='POINT'):
    values = np.array(values).astype('float64')
    mesh = obj.data
    if name not in obj.data.attributes:
        mesh.attributes.new(name=name, type=data_type, domain=domain)
    v = values.flatten()
    mesh.attributes[name].data.foreach_set('vector', v)
    return True

class PointCloudManager(object):
    def __init__(self):
        self.object_manager = ObjectManager()
        return

    def createColor(self, ply_file_path, object_name, color_name='Col'):
        assert os.path.exists(ply_file_path)

        if object_name not in bpy.data.objects.keys():
            print('[WARN][PointCloudManager::createColor]')
            print('\t object not found in blender for object : ' + object_name)
            return True

        obj = bpy.data.objects[object_name]

        point_clouds = o3d.io.read_point_cloud(ply_file_path)
        colors = np.array(point_clouds.colors)[:, :3]

        set_vertex_attr(obj, colors, color_name)
        print('[INFO][PointCloudManager::createColor]')
        print('\t Success for object : ' + object_name)
        return True

    def createColors(self, ply_file_path_list, object_name_list, color_name='Col'):
        for ply_file_path, object_name in zip(ply_file_path_list, object_name_list):
            self.createColor(ply_file_path, object_name, color_name)
        return True

    def createColorsForMethods(self, root_folder_path, method_name_list, object_name_list, color_name='Col'):
        for method_name, object_name in zip(method_name_list, object_name_list):
            ply_folder_path = root_folder_path + method_name + '/'

            ply_filename_list = os.listdir(ply_folder_path)

            max_idx = -1
            latest_ply_filename = None
            for ply_filename in ply_filename_list:
                if '.ply' not in ply_filename:
                    continue

                ply_idx = int(ply_filename.split('.ply')[0].split('_')[-1])
                if ply_idx > max_idx:
                    max_idx = ply_idx
                    latest_ply_filename = ply_filename

            if max_idx == -1:
                print('[WARN][PointCloudManager::createColor]')
                print('\t ply not found for object : ' + object_name)
                continue

            latest_ply_file_path = ply_folder_path + latest_ply_filename

            self.createColor(latest_ply_file_path, object_name, color_name)
        return True