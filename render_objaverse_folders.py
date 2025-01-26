import os
from time import sleep

from blender_manage.Method.tag import clearTag
from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

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

    save_image_folder_path = '/home/chli/chLi/Dataset/Objaverse_82K/render_jpg_test/'

    render_image_num = 12
    workers_per_cpu = 4
    workers_per_gpu = 8
    is_background = True
    mute = True
    gpu_id_list = [0]
    early_stop = False
    overwrite = False

    clear_tag = False

    keep_alive = False

    if clear_tag:
        clearTag(
            tag_folder_path=save_image_folder_path,
            file_format='.jpg',
            dry_run=False,
            worker_num=os.cpu_count(),
        )

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        gpu_id_list,
        early_stop,
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
