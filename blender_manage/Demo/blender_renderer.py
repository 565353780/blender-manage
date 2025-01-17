from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer

def demo():
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/adaptive/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/adaptive/'
    use_gpu = False
    overwrite = False
    is_background = True
    gpu_id = 0
    mute = True
    keep_alive = False

    while True:
        assert BlenderRenderer.isValid()
        process = BlenderRenderer.renderFolders(
            shape_folder_path,
            save_image_folder_path,
            use_gpu,
            overwrite,
            is_background,
            gpu_id,
            mute,
        )

        if process is not None:
            process.start()
            process.join()

        if not keep_alive:
            break
        sleep(1)

    return True
