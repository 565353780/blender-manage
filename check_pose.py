from blender_manage.Module.blender_renderer import BlenderRenderer


def checkFilePose():
    assert BlenderRenderer.isValid()

    shape_file_path = ''
    shape_file_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/bunny/anchor-200/pcd/400_train_pcd.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/295ed09898bf457a9769248f89c33ec1/001/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/840d2861eb4441239d14fc7013c57e79/010/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/3492fec73172474da3e10cb2b682d6c0/005/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/8522724747b24c8397f39ba02bfecb77/009/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/bfc5ba51548b419c94ecf632c0aa9960/004/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/00d1be4411f848efaeb72b936d4d1692/003/iter_1/occ_smooth/sample_1_mesh.ply'

    blender_renderer = BlenderRenderer(
        workers_per_cpu=1,
        workers_per_gpu=0,
        is_background=False,
        mute=False,
        gpu_id_list=[0],
    )

    blender_renderer.checkFilePose(shape_file_path)

    blender_renderer.waitWorkers()
    return True

def checkFolderPose():
    assert BlenderRenderer.isValid()

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

    blender_renderer.checkFolderPose(shape_folder_path)

    blender_renderer.waitWorkers()
    return True



if __name__ == '__main__':
    checkFilePose()
    #checkFolderPose()
