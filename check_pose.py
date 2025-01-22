from blender_manage.Module.blender_renderer import BlenderRenderer


if __name__ == '__main__':
    assert BlenderRenderer.isValid()

    shape_file_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/bunny/anchor-200/pcd/400_train_pcd.ply'
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh/'
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/clip/XiaomiSU7/anc-1500/'
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh/RobotArm/'
    shape_folder_path = '/home/chli/chLi/Results/ma-sh/output/clip/Washer/'

    blender_renderer = BlenderRenderer(
        workers_per_cpu=1,
        workers_per_gpu=0,
        is_background=False,
        mute=False,
        gpu_id_list=[0],
    )

    # blender_renderer.checkFilePose(shape_file_path)
    blender_renderer.checkFolderPose(shape_folder_path)

    blender_renderer.waitWorkers()
