#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Module.shading_manager import ShadingManager

def demo():
    color_map_name = 'morandi'

    shading_manager = ShadingManager()
    shading_manager.paintColorMapForObjects(color_map_name)
    return True
