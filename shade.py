import sys
sys.path.append('/Users/fufu/github/blender-manage')

from blender_manage.Module.shading_manager import ShadingManager

collection_name_list = [
    'GT',
    'ISR+M',
    'VPP-S2C+M',
    'SceneCAD+M',
    'Ours+M',
    'ISR+A',
    'VPP-S2C+A',
    'SceneCAD+A',
    'Ours',
    'ROCA+OurNBV',
    'OurCAD+Guo',
    'OurCAD+Schmid',
    'ours',
    'woop',
    'worp',
    'wither',
]


def demo():
    color_map_name = 'fufu'

    shading_manager = ShadingManager(collection_name_list)
    shading_manager.paintColorMapForObjects(color_map_name)
    return True

if __name__ == '__main__':
    demo()
