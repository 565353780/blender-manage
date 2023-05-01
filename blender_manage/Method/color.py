#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy


def toRGBA(color):
    if isinstance(color, str):
        h = color.lstrip('#')
        rgba = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        rgba.append(255)
        return rgba

    rgba = deepcopy(color)
    if len(rgba) == 3:
        rgba.append(255)
    return rgba


def getColorMap(color_list):
    color_map = {}
    for i, color in enumerate(color_list):
        rgba = toRGBA(color)
        color_map[str(i)] = rgba
    return color_map
