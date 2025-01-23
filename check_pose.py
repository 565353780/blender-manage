from blender_manage.Module.blender_renderer import BlenderRenderer


def checkFilePose():
    assert BlenderRenderer.isValid()

    shape_file_path = '/home/chli/chLi/Results/ma-sh/output/fit/fixed/bunny/anchor-200/pcd/400_train_pcd.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/295ed09898bf457a9769248f89c33ec1/001/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/840d2861eb4441239d14fc7013c57e79/010/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/3492fec73172474da3e10cb2b682d6c0/005/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/8522724747b24c8397f39ba02bfecb77/009/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_14:38:06/dino/000-000/bfc5ba51548b419c94ecf632c0aa9960/004/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/00d1be4411f848efaeb72b936d4d1692/003/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/02b63726c08a4604b5c6f4240dc31786/006/iter_1/pcd/sample_1_pcd.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/003ebdf86df345d39dc166563229fb85/004/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/04a47d898e704e1a809d24433c409bf5/005/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/06e62743a034421f843d88175c87d916/009/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/009fdf73a9c54e7bbd3a7d28496752e0/006/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/013bf202170542e3a952fe810e72d385/007/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/31f4edaa55d04dc58599b8d16c1bc073/003/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/038d1eeb927d442bb0b8f9100ad7dbb2/010/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/45e3468808f844e8b56826655a2573f7/006/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/057dd0154cbc47549c73a092aa15199e/001/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/87a7bb85433843059c1299ac2cd2fe7f/005/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/0238adfcca3e4727b9c36eba3a9eb7cb/011/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/0364ceec22904a95847edea62ad1e9fd/003/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/0413d92d70f24a68b3afe8643301c515/000/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/c31dc47768c64cb6b6b31397964e80a0/006/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/c97116812b4848c3ad79432718caaf29/006/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/d2d2287ced8845259fca57d0eb34761b/008/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/e3737d42c06242f8995f9381aa1e635d/005/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-000/ebeab69af57442048e64cecee41465a7/005/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-001/6f1f320e0f1c400d9f6c25e6de7bef6a/005/iter_1/pcd/sample_4_pcd.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-001/46e64593c4234183b3b00391fc960415/001/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-001/cdf4325abc5d4780b14c33382c3f2764/010/iter_1/occ_smooth/sample_3_mesh.ply '
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_15:00:12/dino/000-002/dacdcecd681f47898164085ec1eb5ef3/010/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_17:39:42/dino/000-000/1c5b59a3e74b468d875d670d8f3fe7d0/007/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250122_17:39:42/dino/000-000/04c27525c52748b8a0dead78a14e2f58/011/iter_1/pcd/sample_4_pcd.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/5b5a102914d940099b89dd787f2a6ef8/005/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/2e106aee209545f0b79eb3618ab29ed0/010/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/6fb99a87667c4bd0849c641f2fdcbf30/005/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/7a46167ec0534c00ab14c8d73f186618/004/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/9caaa68869454b21b75e92bc12762acf/005/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/19a3321b01224d20bfe06b210b74e79a/002/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/457e039fa457408dbf666a60e6ba8cbc/010/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/685b601b57554410b2050acbc04e226f/005/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/8613078b95364c29b9d54db6d641ad27/007/iter_1/occ_smooth/sample_2_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-001/c2e195b7c1aa49c792a9051ec62ba2a2/009/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/6c2662fe52584bceab560f0bd9efcf51/005/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/66c065a0cf3f4fc881e00607a86b0f69/009/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/357d38c4a6344c518a5e01687dbcd84b/010/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/812ab586264e463dafc7072a8ab47779/010/iter_1/occ_smooth/sample_4_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/078912b3b27747e5bad669a82e2c02ac/007/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/b00db85422d248f38bb17ae9a6af59f0/010/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/b3b722d4664b474c9da13e87e0d0c598/003/iter_1/occ_smooth/sample_3_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/e1a2232644da48978fddf39544596f42/005/iter_1/occ_smooth/sample_1_mesh.ply'
    shape_file_path = '/Users/fufu/Downloads/Dataset/MashDiffusion/sample/20250123_10:07:02/dino/000-002/f8af9ffc678e40c5b38908f690a555a8/005/iter_1/occ_smooth/sample_2_mesh.ply'

    shape_file_path = '/Users/fufu/Downloads/0121_1/Hunyuan3D-1_compare/01/mesh_vertex_colors.obj'

    #shape_file_path = ''
    #shape_file_path = '/Users/fufu/Downloads/bunny/anchor-50/mash/0_train_anc-50_mash.ply'


    #shape_file_path = '/Users/fufu/Downloads/parts/02691156/a75a/sample_73_mesh.ply'

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
