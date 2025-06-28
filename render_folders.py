import os
from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer

home = os.environ["HOME"]

shape_data_dict = {
    "RobotArm": [
        home + "/chLi/Results/ma-sh/output/fit/fixed/RobotArm/",
        home + "/chLi/Results/ma-sh/output/fit_render/fixed/RobotArm/",
    ],
    "Thingi10K-46602": [
        home + "/chLi/Results/render/Thingi10K/46602/",
        home + "/chLi/Results/render/Thingi10K/render/46602/",
    ],
    "Thingi10K-61258": [
        home + "/chLi/Results/render/Thingi10K/61258/",
        home + "/chLi/Results/render/Thingi10K/render/61258/",
    ],
    "KITTI": [
        home + "/chLi/Results/render/KITTI/",
        home + "/chLi/Results/render/KITTI_render/",
    ],
    "Bunny-50anc": [
        home + "/chLi/Results/ma-sh/output/fit_error_mesh/bunny/anchor-50/",
        home
        + "/chLi/Results/ma-sh/output/fit_error_mesh_render/bunny/anchor-50_1000x1000/",
    ],
    "XiaomiSU7": [
        home + "/chLi/Results/ma-sh/output/crop/XiaomiSU7/",
        home + "/chLi/Results/ma-sh/output/render_crop/XiaomiSU7_1000x1000/",
    ],
    "Washer": [
        home + "/chLi/Results/ma-sh/output/crop/Washer/",
        home + "/chLi/Results/ma-sh/output/render_crop/Washer_1000x1000/",
    ],
    "vae-eval": [
        home + "/chLi/Dataset/vae-eval/render_pcd/",
        home + "/chLi/Dataset/vae-eval/manifold_mash_render-4000anc/",
    ],
    "TRELLIS": [
        home + "/chLi/Dataset/TRELLIS/mash_gen_process/",
        home + "/chLi/Dataset/TRELLIS/render_mash_gen_process/",
    ],
}

if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    shape_folder_path, save_image_folder_path = shape_data_dict["TRELLIS"]

    workers_per_cpu = 1
    workers_per_gpu = 8
    is_background = True
    mute = True
    gpu_id_list = [0, 1, 2, 3, 4, 5, 6, 7]
    early_stop = False
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
