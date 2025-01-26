from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    shape_file_path = '/home/chli/chLi/Dataset/Famous/normalized_mesh/bunny.ply'
    save_image_file_path = '/home/chli/chLi/Dataset/Famous/render_normalized_mesh/bunny.png'

    workers_per_cpu = 4
    workers_per_gpu = 8
    is_background = True
    mute = True
    gpu_id_list = [0]
    overwrite = True
    early_stop = False

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        gpu_id_list,
        early_stop,
    )

    blender_renderer.renderFile(
        shape_file_path,
        save_image_file_path,
        overwrite,
    )

    blender_renderer.waitWorkers()
