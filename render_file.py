from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    shape_file_path = '/home/chli/chLi/Dataset/Famous/normalized_mesh/bunny.ply'
    save_image_file_path = '/home/chli/chLi/Dataset/Famous/render_normalized_mesh/bunny.png'

    workers_per_cpu = 0
    workers_per_gpu = 1
    is_background = True
    mute = True
    gpu_id_list = [0]
    overwrite = True

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        gpu_id_list,
    )

    blender_renderer.renderFile(
        shape_file_path,
        save_image_file_path,
        overwrite,
    )

    blender_renderer.waitWorkers()
