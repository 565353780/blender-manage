#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import pow
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
        if color[0] == '#':
            hex_str = color[1:]
        else:
            hex_str = color
        rgba = [int(hex_str[i:i + 2], 16) for i in [0, 2, 4]]
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

def toLinearRGBValue(rgb_value):
    if rgb_value <= 0.0405:
        return rgb_value / 12.92
    return pow((rgb_value + 0.055) / 1.055, 2.4)

def toLinearRGBA(color):
    rgba = toRGBA(color)

    float_rgba = rgba.astype(float) / 255.0

    linear_rgba = []
    for i in range(3):
        linear_rgba.append(toLinearRGBValue(float_rgba[i]))

    linear_rgba.append(float_rgba[3])

    linear_rgba = np.array(linear_rgba, dtype=float)
    return linear_rgba

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
        rgba = toLinearRGBA(color)
        color_map[str(i)] = rgba
    return color_map
