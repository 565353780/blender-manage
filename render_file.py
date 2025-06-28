from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    workers_per_cpu = 1
    workers_per_gpu = 0
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

    shape_file_path = "/Users/chli/chLi/Dataset/TRELLIS/mash_gen_process/000b76f2b03e44e8ab44e1a1614be0f4/20_train_pcd.ply"
    save_image_file_path = "/Users/chli/chLi/Dataset/TRELLIS/render_mash_gen_process/000b76f2b03e44e8ab44e1a1614be0f4/20_train_pcd.png"

    blender_renderer.renderFile(
        shape_file_path,
        save_image_file_path,
        overwrite,
    )

    blender_renderer.waitWorkers()
