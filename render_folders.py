from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/Bunny/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/Bunny/'
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/'
    workers_per_cpu = 1
    workers_per_gpu = 0
    is_background = True
    mute = True
    gpu_id_list = [0]
    overwrite = True

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
