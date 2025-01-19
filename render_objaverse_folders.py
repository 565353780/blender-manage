import os
import argparse
from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    parser = argparse.ArgumentParser(description="Render Objaverse Folders")
    parser.add_argument(
        '--workers_per_cpu',
        type=int,
        default=4,
    )
    parser.add_argument(
        '--workers_per_gpu',
        type=int,
        default=8,
    )
    parser.add_argument(
        '--gpu_id_list',
        type=int,
        nargs='+',
        default=[0],
        help="List of GPU IDs to use, e.g., --gpu_ids 0 1 2"
    )
    args = parser.parse_args()

    dataset_folder_path_list = [
        '/home/chli/chLi/Dataset/Objaverse_82K/glbs/',
        '/mnt/d/chLi/Dataset/Objaverse_82K/glbs/',
        '/mnt/data/jintian/chLi/Dataset/Objaverse_82K/glbs/',
    ]

    shape_folder_path = None
    for dataset_folder_path in dataset_folder_path_list:
        if os.path.exists(dataset_folder_path):
            shape_folder_path = dataset_folder_path
            break

    if shape_folder_path is None:
        print('dataset not found!')
        exit()

    render_image_num = 12
    save_image_folder_path = shape_folder_path.replace('/glbs/', '/render_jpg_v2/')
    workers_per_cpu = args.workers_per_cpu
    workers_per_gpu = args.workers_per_gpu
    is_background = True
    mute = True
    use_gpu = True
    gpu_id_list = args.gpu_id_list
    overwrite = False
    keep_alive = False

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        use_gpu,
        gpu_id_list,
    )

    while True:
        blender_renderer.renderAroundObjaverseFolders(
            shape_folder_path,
            render_image_num,
            save_image_folder_path,
            overwrite,
        )

        blender_renderer.waitWorkers()

        if not keep_alive:
            break
        sleep(1)
