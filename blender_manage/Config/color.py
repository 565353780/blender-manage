#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Method.color import getColorMap

macaron_color_list = [
    "#FBB5AF", "#FBE06F", "#B0E586", "#8AD4D5", "#718DD5", "#A38DDE",
    "#9ED68C", "#61abff", "#ffb056", '#A9CBFF', "#7a7579", "#a59b95",
    "#dcd7d9", "#cb9c7a", "#8a7b93", "#dcd2bd", "#755953", "#efedeb",
    "#d8d1e1", "#cdb97d", "#ddd7d3", "#7d90a5", "#d1bfac", "#7f8d7b",
    "#c6cee2", "#f1dadb", "#af777e", "#c5bdb7", "#969696", "#9aa193",
    "#fffbe8", "#cadabd", "#e7d8d4", "#e8e8dc", "#bdbab2", "#d9d6d9",
    "#f1dfde", "#e3dca3", "#dcd2bd", "#fbeede", "#a1b2cc", "#a59b95",
    "#f18772", "#6c696a", "#a54b43", "#d8d0be", "#b0886a", "#cbcbc9", "#686954"
]

morandi_color_list = [
    "#f5cec7", "#e79796", "#ffc98b", "#ffb284", "#c6c09e", "#80beaf",
    "#b3ddd1", "#d1dce2", "#f5b994", "#ee9c6c", "#86e4cc", "#d0e6a5",
    "#ffdd95", "#fa897b", "#ccabd8", "#fbd5e0", "#eeecef", "#ade2cc",
    "#fcc523", "#f9615e", "#f7b5ce", "#8fdbd7", "#b6dfa5", "#12b391",
    "#fa74a7", "#ffa9c4", "#f9edd3", "#f6d7c3", "#acbeec", "#c8d5f7",
    "#fed6de", "#fec5ce", "#ffadbb", "#e3f7eb", "#d3e9f6"
]

COLOR_MAP_DICT = {
    'macaron': getColorMap(macaron_color_list),
    'morandi': getColorMap(morandi_color_list),
}
