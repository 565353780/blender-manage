import os

from blender_manage.Method.tag import clearTag



if __name__ == "__main__":
    dataset_folder_path_list = [
        '/home/chli/chLi/Dataset/Objaverse_82K/render_jpg_v2/',
        '/mnt/d/chLi/Dataset/Objaverse_82K/render_jpg_v2/',
        '/mnt/data/jintian/chLi/Dataset/Objaverse_82K/render_jpg_v2/',
    ]

    shape_folder_path = None
    for dataset_folder_path in dataset_folder_path_list:
        if os.path.exists(dataset_folder_path):
            shape_folder_path = dataset_folder_path
            break

    if shape_folder_path is None:
        print('dataset not found!')
        exit()

    dry_run = False
    worker_num = os.cpu_count()

    clearTag(shape_folder_path, '.jpg', dry_run, worker_num)
