from blender_manage.Method.video import toVideo, toGif


if __name__ == '__main__':
    fps = 30
    overwrite = False

    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/bunny/anchor-50/pcd/',
        '/home/chli/chLi/Results/ma-sh/output/video/bunny_anchor-50.mp4',
        fps,
        overwrite,
    )

    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh_render/bunny/anchor-50/mash/',
        '/home/chli/chLi/Results/ma-sh/output/video/bunny_anchor-50_error.mp4',
        fps,
        overwrite,
    )

    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/render_crop/XiaomiSU7/anc-1500/',
        '/home/chli/chLi/Results/ma-sh/output/video/XiaomiSU7_crop.mp4',
        fps,
        overwrite,
    )

    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/render_crop/Washer/anc-1500/',
        '/home/chli/chLi/Results/ma-sh/output/video/Washer_crop.mp4',
        fps,
        overwrite,
    )
