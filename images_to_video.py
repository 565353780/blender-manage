from blender_manage.Method.video import toVideo, toGif


if __name__ == '__main__':
    fps = 10
    overwrite = False

    toGif(
        '/home/chli/chLi/Dataset/Thingi10K/mesh_render/46602/',
        '/home/chli/chLi/Dataset/Thingi10K/gif/mesh_46602.gif',
        fps,
        overwrite,
    )

    toGif(
        '/home/chli/chLi/Dataset/Thingi10K/mesh_render/61258/',
        '/home/chli/chLi/Dataset/Thingi10K/gif/mesh_61258.gif',
        fps,
        overwrite,
    )

    toGif(
        '/home/chli/chLi/Dataset/Thingi10K/mash_render/46602_tmp_1_xyz/',
        '/home/chli/chLi/Dataset/Thingi10K/gif/mash_46602.gif',
        fps,
        overwrite,
    )

    toGif(
        '/home/chli/chLi/Dataset/Thingi10K/mash_render/61258_tmp_1_xyz/',
        '/home/chli/chLi/Dataset/Thingi10K/gif/mash_61258.gif',
        fps,
        overwrite,
    )
