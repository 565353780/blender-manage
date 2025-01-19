import argparse
from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--gpu_id",
        type=int,
        default=0,
    )

    args = parser.parse_args()

    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/XiaomiSU7/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/XiaomiSU7/'
    use_gpu = False
    overwrite = True
    is_background = True
    gpu_id = args.gpu_id
    mute = True
    with_daemon = True
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
            with_daemon,
        )

        if process is not None:
            process.start()
            process.join()

        if not keep_alive:
            break
        sleep(1)
