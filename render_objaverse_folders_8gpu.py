import os
from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
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

    # shape_folder_path = '/home/chli/chLi/Dataset/Objaverse_82K/glbs/'
    render_image_num = 12
    save_image_folder_path = shape_folder_path.replace('/glbs/', '/render_jpg_v2/')
    use_gpu = True
    overwrite = False
    is_background = True
    gpu_id_list = [0, 1, 2, 3, 4, 5, 6, 7]
    workers_per_gpu = 6
    mute = True
    keep_alive = False

    while True:
        assert BlenderRenderer.isValid()
        BlenderRenderer.parallelRenderAroundObjaverseFolders(
            shape_folder_path,
            render_image_num,
            save_image_folder_path,
            use_gpu,
            overwrite,
            is_background,
            gpu_id_list,
            workers_per_gpu,
            mute,
        )

        if not keep_alive:
            break
        sleep(1)
