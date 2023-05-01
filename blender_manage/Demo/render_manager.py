#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Module.render_manager import RenderManager

def demo():
    color_map_name = 'morandi'

    render_manager = RenderManager()

    render_manager.renderAllViews()
    return True
