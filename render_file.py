from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    shape_file_path = '/home/chli/chLi/Dataset/Famous/normalized_mesh/bunny.ply'
    save_image_file_path = '/home/chli/chLi/Dataset/Famous/render_normalized_mesh/bunny.png'

    shape_file_path_11 = '/home/chli/chLi/Dataset/Thingi10K/mesh/46602.obj'
    shape_file_path_12 = '/home/chli/chLi/Dataset/Thingi10K/mesh/61258.obj'
    save_image_file_path_1 = '/home/chli/chLi/Dataset/Thingi10K/mesh_render/'

    shape_file_path_21 = '/home/chli/chLi/Dataset/Thingi10K/mesh_mash_recon-1600anc/46602_tmp_1_xyz.xyz'
    shape_file_path_22 = '/home/chli/chLi/Dataset/Thingi10K/mesh_mash_recon-1600anc/61258_tmp_1_xyz.xyz'
    save_image_file_path_2 = '/home/chli/chLi/Dataset/Thingi10K/mash_render/'

    workers_per_cpu = 4
    workers_per_gpu = 0
    is_background = True
    mute = True
    gpu_id_list = [0]
    early_stop = False
    overwrite = True

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        gpu_id_list,
        early_stop,
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

    blender_renderer.renderAroundFile(
        shape_file_path_21,
        60,
        save_image_file_path_2,
        overwrite,
    )

    blender_renderer.renderAroundFile(
        shape_file_path_22,
        60,
        save_image_file_path_2,
        overwrite,
    )

    blender_renderer.waitWorkers()
