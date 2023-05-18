#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

def isIntValue(value_list):
    for value in value_list:
        if value != int(value):
            return False

    return True

def toRGBA(color):
    if isinstance(color, str):
        h = color.lstrip('#')
        rgba = [float(int(h[i:i + 2], 16)) / 255.0 for i in (0, 2, 4)]
        rgba.append(1.0)
        return rgba

    rgba = deepcopy(color)

    if isIntValue(rgba):
        for i in range(len(rgba)):
            rgba[i] = float(rgba[i]) / 255.0

    if len(rgba) == 3:
        rgba.append(1.0)
    return rgba

def toIntRGBA(color):
    rgba = toRGBA(color)

    int_rgba = [int(value * 255.0) for value in rgba]
    return int_rgba

def toHex(color):
    rgba = toRGBA(color)

    hex_str = '#'
    for i in range(3):
        color_value = int(rgba[i] * 255.0)
        current_hex_str = '{:02X}'.format(color_value)
        hex_str += current_hex_str
    return hex_str

def getColorMap(color_list):
    color_map = {}
    for i, color in enumerate(color_list):
        rgba = toRGBA(color)
        color_map[str(i)] = rgba
    return color_map
