#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from copy import deepcopy

def isIntValue(value_list):
    for value in value_list:
        if value != int(value):
            return False

    for value in value_list:
        if isinstance(value, float):
            return False

    return True

def toRGBA(color):
    if isinstance(color, str):
        h = color.lstrip('#')
        rgba = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        rgba.append(255)
        rgba = np.array(rgba, dtype=np.uint8)
        return rgba

    rgba = []

    if isIntValue(color):
        for i in range(len(color)):
            rgba.append(int(color[i]))
    else:
        for i in range(len(color)):
            rgba.append(int(float(color[i]) * 255.0))

    if len(rgba) == 3:
        rgba.append(255)

    rgba = np.array(rgba, dtype=np.uint8)
    return rgba

def toHex(color):
    rgba = toRGBA(color)

    hex_str = '#'
    for i in range(3):
        current_hex_str = '{:02X}'.format(rgba[i])
        hex_str += current_hex_str
    return hex_str

def getColorMap(color_list):
    color_map = {}
    for i, color in enumerate(color_list):
        rgba = toRGBA(color)
        color_map[str(i)] = rgba
    return color_map
