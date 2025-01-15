from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer

def demo():
    time_stamp = '20250115_19:44:22'
    shape_folder_path = '/home/chli/chLi/Results/mash-diffusion/output/sample/' + time_stamp + '/'
    save_image_folder_path = '/home/chli/chLi/Results/mash-diffusion/output/render/' + time_stamp + '/'
    use_gpu = False
    overwrite = False
    keep_alive = True

    '''
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/adaptive/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/adaptive/'
    '''

    while True:
        blender_renderer = BlenderRenderer()
        blender_renderer.renderFolders(shape_folder_path, save_image_folder_path, use_gpu, overwrite)

        if not keep_alive:
            break
        sleep(1)

    return True
