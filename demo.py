import sys
sys.path.append('/Users/fufu/github/blender-manage')

from blender_manage.Demo.object_manager import demo as demo_manage_object
from blender_manage.Demo.shading_manager import demo as demo_manage_shading
from blender_manage.Demo.render_manager import demo as demo_manage_render
from blender_manage.Demo.pointcloud_manager import demo as demo_manage_pointcloud

if __name__ == '__main__':
    #  demo_manage_object()
    #  demo_manage_shading()
    demo_manage_render()
    #  demo_manage_pointcloud()
