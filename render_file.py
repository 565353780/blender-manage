from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    from custom_path import data_dict, thingi10k_fit_shape_id_list

    shape_id_list = thingi10k_fit_shape_id_list

    workers_per_cpu = 1
    workers_per_gpu = 6
    is_background = True
    mute = True
    gpu_id_list = [0]
    early_stop = False
    overwrite = False

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        gpu_id_list,
        early_stop,
    )

    '''
    blender_renderer.renderFile(
        shape_file_path,
        save_image_file_path,
        overwrite,
    )

    blender_renderer.renderAroundFile(
        shape_file_path_11,
        60,
        save_image_file_path_1,
        overwrite,
    )

    blender_renderer.renderAroundFile(
        shape_file_path_12,
        60,
        save_image_file_path_1,
        overwrite,
    )
    '''

    for shape_id in shape_id_list:
        shape_file_path = data_dict[shape_id][0]
        save_image_folder_path = data_dict[shape_id][1]

        blender_renderer.renderAroundFile(
            shape_file_path,
            60,
            save_image_folder_path,
            overwrite,
        )

    blender_renderer.waitWorkers()
