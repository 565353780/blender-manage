import argparse
from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--gpu_id",
        type=int,
        required=True,
    )

    args = parser.parse_args()

    shape_folder_path = '/home/chli/chLi/Dataset/Objaverse_82K/glbs/'
    render_image_num = 12
    save_image_folder_path = '/home/chli/chLi/Dataset/Objaverse_82K/render_jpg_v2/'
    use_gpu = True
    overwrite = False
    is_background = True
    gpu_id = args.gpu_id
    mute = True
    keep_alive = False

    while True:
        assert BlenderRenderer.isValid()
        process = BlenderRenderer.renderAroundObjaverseFolders(
            shape_folder_path,
            render_image_num,
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
