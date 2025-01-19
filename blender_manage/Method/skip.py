import os


def skip_func_renderAroundObjaverse(python_args_dict: dict) -> bool:
    shape_file_path = python_args_dict['shape_file_path']
    render_image_num = python_args_dict['render_image_num']
    save_image_folder_path = python_args_dict['save_image_folder_path']

    object_name = shape_file_path.split('/')[-1].split('.')[0]
    new_save_image_folder_path = save_image_folder_path + object_name + '/'

    start_tag_file_path = new_save_image_folder_path + 'start.txt'

    if os.path.exists(start_tag_file_path):
        return True

    for i in range(render_image_num):
        save_image_file_path = new_save_image_folder_path + f"{i:03d}.jpg"
        if not os.path.exists(save_image_file_path):
            return False

    return True
