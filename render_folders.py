from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer


shape_data_dict = {
    "RobotArm": [
        "/home/chli/chLi/Results/ma-sh/output/fit/fixed/RobotArm/",
        "/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/RobotArm/",
    ],
    "Thingi10K-46602": [
        "/home/chli/chLi/Results/render/Thingi10K/46602/",
        "/home/chli/chLi/Results/render/Thingi10K/render/46602/",
    ],
    "Thingi10K-61258": [
        "/home/chli/chLi/Results/render/Thingi10K/61258/",
        "/home/chli/chLi/Results/render/Thingi10K/render/61258/",
    ],
    "KITTI": [
        "/home/chli/chLi/Results/render/KITTI/",
        "/home/chli/chLi/Results/render/KITTI_render/",
    ],
    "Bunny-50anc": [
        "/home/chli/chLi/Results/ma-sh/output/fit_error_mesh/bunny/anchor-50/",
        "/home/chli/chLi/Results/ma-sh/output/fit_error_mesh_render/bunny/anchor-50_1000x1000/",
    ],
    "XiaomiSU7": [
        "/home/chli/chLi/Results/ma-sh/output/crop/XiaomiSU7/",
        "/home/chli/chLi/Results/ma-sh/output/render_crop/XiaomiSU7_1000x1000/",
    ],
    "Washer": [
        "/home/chli/chLi/Results/ma-sh/output/crop/Washer/",
        "/home/chli/chLi/Results/ma-sh/output/render_crop/Washer_1000x1000/",
    ],
    "vae-eval": [
        "/home/chli/chLi/Dataset/vae-eval/render_pcd/",
        "/home/chli/chLi/Dataset/vae-eval/manifold_mash_render-4000anc/",
    ],
}

if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    from custom_path import data_dict, s2v_gen_shape_id_list as shape_id_list

    shape_folder_path, save_image_folder_path = shape_data_dict["vae-eval"]

    workers_per_cpu = 1
    workers_per_gpu = 6
    is_background = True
    mute = True
    gpu_id_list = [0]
    early_stop = True
    overwrite = False

    keep_alive = False

    blender_renderer = BlenderRenderer(
        workers_per_cpu,
        workers_per_gpu,
        is_background,
        mute,
        gpu_id_list,
        early_stop,
    )

    blender_renderer.renderFolders(
        shape_folder_path,
        save_image_folder_path,
        overwrite,
    )

    blender_renderer.waitWorkers()
    exit()

    while True:
        for shape_id in shape_id_list:
            shape_folder_path = data_dict[shape_id][0]
            save_image_folder_path = data_dict[shape_id][1]

            blender_renderer.renderFolders(
                shape_folder_path,
                save_image_folder_path,
                overwrite,
            )

        blender_renderer.waitWorkers()

        if not keep_alive:
            break
        sleep(1)
