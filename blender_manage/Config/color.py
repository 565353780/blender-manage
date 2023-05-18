#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blender_manage.Method.color import getColorMap

old_macaron_color_list = [
    "#FBB5AF", "#FBE06F", "#B0E586", "#8AD4D5", "#718DD5", "#A38DDE",
    "#9ED68C", "#61abff", "#ffb056", '#A9CBFF', "#7a7579", "#a59b95",
    "#dcd7d9", "#cb9c7a", "#8a7b93", "#dcd2bd", "#755953", "#efedeb",
    "#d8d1e1", "#cdb97d", "#ddd7d3", "#7d90a5", "#d1bfac", "#7f8d7b",
    "#c6cee2", "#f1dadb", "#af777e", "#c5bdb7", "#969696", "#9aa193",
    "#fffbe8", "#cadabd", "#e7d8d4", "#e8e8dc", "#bdbab2", "#d9d6d9",
    "#f1dfde", "#e3dca3", "#dcd2bd", "#fbeede", "#a1b2cc", "#a59b95",
    "#f18772", "#6c696a", "#a54b43", "#d8d0be", "#b0886a", "#cbcbc9", "#686954"
]

macaron_color_list = [
    '#f1707d', '#f155369', '#ef5767', '#ae716e', '#cb8e85', '#cf8878', '#cf8878',
    '#f1ccb8', '#f2debd', '#b8d38f', '#ddff95', '#ff9b6a', '#f1b8f1', '#d9b8f1',
    '#f1ccb8', '#f1f1b8', '#b8f1ed', '#b8f1cc', '#e7dbca', '#e26538', '#f3d751',
    '#fd803a', '#fe997b', '#c490a0', '#f28a63', '#df7a30', '#e96d29', '#cb7799',
    '#e3a04f', '#edc02f', '#fecf45', '#f9b747', '#c28164', '#ed987b', '#ffe647',
    '#e49f5e', '#ff8444', '#ac5e74', '#f0b735', '#d08a8a'
]

morandi_color_list = [
    "#f5cec7", "#e79796", "#ffc98b", "#ffb284", "#c6c09e", "#80beaf",
    "#b3ddd1", "#d1dce2", "#f5b994", "#ee9c6c", "#86e4cc", "#d0e6a5",
    "#ffdd95", "#fa897b", "#ccabd8", "#fbd5e0", "#eeecef", "#ade2cc",
    "#fcc523", "#f9615e", "#f7b5ce", "#8fdbd7", "#b6dfa5", "#12b391",
    "#fa74a7", "#ffa9c4", "#f9edd3", "#f6d7c3", "#acbeec", "#c8d5f7",
    "#fed6de", "#fec5ce", "#ffadbb", "#e3f7eb", "#d3e9f6"
]

juzhan_color_list = [
    "#FBB5AF", "#FBE06F", "#B0E586", "#8AD4D5", "#718DD5", "#A38DDE",
    "#9ED68C", "#61abff", "#ffb056", '#A9CBFF'
]

source_color_list = [
    '#FFB6C1', '#FFC0CB', '#DC143C', '#FFF0F5', '#DB7093', '#FF69B4',
    '#FF1493', '#C71585', '#DA70D6', '#D8BFD8', '#DDA0DD', '#EE82EE',
    '#FF00FF', '#FF00FF', '#8B008B', '#800080', '#BA55D3', '#9400D3',
    '#9932CC', '#4B0082', '#8A2BE2', '#9370DB', '#7B68EE', '#6A5ACD',
    '#483D8B', '#E6E6FA', '#F8F8FF', '#0000FF', '#0000FF', '#0000CD',
    '#191970', '#00008B', '#000080', '#4169E1', '#6495ED', '#B0C4DE',
    '#778899', '#708090', '#1E90FF', '#F0F8FF', '#4682B4', '#87CEFA',
    '#87CEEB', '#00BFFF', '#ADD8E6', '#B0E0E6', '#5F9EA0', '#F0FFFF',
    '#E1FFFF', '#AFEEEE', '#00FFFF', '#00FFFF', '#00CED1', '#2F4F4F',
    '#008B8B', '#008080', '#48D1CC', '#20B2AA', '#40E0D0', '#7FFFAA',
    '#00FA9A', '#F5FFFA', '#00FF7F', '#3CB371', '#2E8B57', '#F0FFF0',
    '#90EE90', '#98FB98', '#8FBC8F', '#32CD32', '#00FF00', '#228B22',
    '#00FF00', '#006400', '#7FFF00', '#7CFC00', '#ADFF2F', '#556B2F',
    '#6B8E23', '#FAFAD2', '#FFFFF0', '#FFFFE0', '#FFFF00', '#FFFF00',
    '#808000', '#BDB76B', '#FFFACD', '#EEE8AA', '#F0E68C', '#FFD700',
    '#FFF8DC', '#DAA520', '#FFFAF0', '#FDF5E6', '#F5DEB3', '#FFE4B5',
    '#FFA500', '#FFEFD5', '#FFEBCD', '#FFDEAD', '#FAEBD7', '#D2B48C',
    '#DEB887', '#FFE4C4', '#FF8C00', '#FAF0E6', '#CD853F', '#FFDAB9',
    '#F4A460', '#D2691E', '#8B4513', '#FFF5EE', '#A0522D', '#FFA07A',
    '#FF7F50', '#FF4500', '#E9967A', '#FF6347', '#FFE4E1', '#FA8072',
    '#FFFAFA', '#F08080', '#BC8F8F', '#CD5C5C', '#FF0000', '#A52A2A',
    '#B22222', '#8B0000', '#800000', '#FFFFFF', '#F5F5F5', '#DCDCDC',
    '#D3D3D3', '#C0C0C0', '#A9A9A9', '#808080', '#696969', '#000000',
]

fufu_color_list = [
    '#3299cc', '#32cd32', '#db70db', '#ff7f00', '#4d4dff', '#7fff00',
    '#9370db', '#adeaea', '#ffff3d', '#7093db', '#9f5f9f', '#70dbdb',
    '#e47833', '#FBB5AF', '#856363', '#8e6b23',
]

junfu_color_list = [
    '#61ABFF', '#6B5152', '#7A7281', '#FBE06F', '#B0E586', '#8AD4D5',
    '#A9CBFF', '#FFB056', '#A38DDE', '#B5C4B1', '#9ED68C', '#FBB5AF',
    '#718DD5', '#A38DDE', '#B5C4B1', '#A6A6A8',
]

COLOR_MAP_DICT = {
    'old_macaron': getColorMap(old_macaron_color_list),
    'macaron': getColorMap(macaron_color_list),
    'morandi': getColorMap(morandi_color_list),
    'juzhan': getColorMap(juzhan_color_list),
    'source': getColorMap(source_color_list),
    'fufu': getColorMap(fufu_color_list),
    'junfu': getColorMap(junfu_color_list),
}
