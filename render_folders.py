from time import sleep

from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == "__main__":
    assert BlenderRenderer.isValid()

    # shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/bunny/anchor-50/'
    # save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/bunny/anchor-50/'

    #shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh/'
    #save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh_render/'

    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/RobotArm/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/RobotArm/'

    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/clip/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/render_clip/'

    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit/test/'
    save_image_folder_path = '/home/chli/chLi/Results/ma-sh/output/render_fit_test/'

    shape_folder_path = '/home/chli/chLi/Dataset/Thingi10K/mesh/'
    save_image_folder_path = '/home/chli/chLi/Dataset/Thingi10K/mesh_render/'

    workers_per_cpu = 4
    workers_per_gpu = 8
    is_background = True
    mute = True
    gpu_id_list = [0]
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

    while True:
        blender_renderer.renderFolders(
            shape_folder_path,
            save_image_folder_path,
            overwrite,
        )

        blender_renderer.waitWorkers()

        if not keep_alive:
            break
        sleep(1)
