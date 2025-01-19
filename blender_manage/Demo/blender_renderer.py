from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer

def demo():
    assert BlenderRenderer.isValid()

    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/adaptive/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/adaptive/'
    workers_per_cpu = 8
    workers_per_gpu = 8
    is_background = True
    mute = True
    gpu_id_list = [0]
    overwrite = False

    keep_alive = False

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        gpu_id_list,
    )

    while True:
        blender_renderer.renderFolders(
            shape_folder_path,
            save_image_folder_path,
            overwrite,
        )

        blender_renderer.waitWorkers()

        if not keep_alive:
            break
        sleep(1)

    return True
