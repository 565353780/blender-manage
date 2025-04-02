from blender_manage.Method.video import toVideo, toGif


def demo():
    image_folder_path = '/users/fufu/nutstore files/my-materials/20250210_china3dv演讲ppt/materials/bunny-sh-fitting_render/'
    save_video_file_path = '/users/fufu/nutstore files/my-materials/20250210_china3dv演讲ppt/materials/video_bunny-sh-fitting.mp4'

    image_folder_path = '/users/fufu/nutstore files/my-materials/20250210_china3dv演讲ppt/materials/bunny-anchor-fitting_render/'
    save_video_file_path = '/users/fufu/nutstore files/my-materials/20250210_China3DV演讲PPT/materials/video_bunny-Anchor-fitting.mp4'

    image_folder_path = '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/sample_directions_1/'
    save_video_file_path = '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/video_sample_directions_1.gif'

    image_folder_path = '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/sample_directions_2/'
    save_video_file_path = '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/video_sample_directions_2.gif'

    fps = 10
    overwrite = False

    toVideo(
        image_folder_path,
        save_video_file_path,
        fps,
        overwrite,
    )

    toGif(
        '/Users/fufu/Downloads/Dataset/Thingi10K/mesh_render/46602/',
        '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/high_genus/46602_mesh.gif',
        fps,
        overwrite,
    )
    toGif(
        '/Users/fufu/Downloads/Dataset/Thingi10K/mesh_render/61258/',
        '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/high_genus/61258_mesh.gif',
        fps,
        overwrite,
    )
    toGif(
        '/Users/fufu/Downloads/Dataset/Thingi10K/mash_render/46602_tmp_1_xyz/',
        '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/high_genus/46602_mash.gif',
        fps,
        overwrite,
    )
    toGif(
        '/Users/fufu/Downloads/Dataset/Thingi10K/mash_render/61258_tmp_1_xyz/',
        '/Users/fufu/Nutstore Files/My-Materials/20250210_China3DV演讲PPT/materials/high_genus/61258_mash.gif',
        fps,
        overwrite,
    )
