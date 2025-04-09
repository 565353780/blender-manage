from blender_manage.Method.video import toVideo, toGif


if __name__ == '__main__':
    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/fit_render/fixed/bunny/anchor-50_1000x1000/pcd/',
        '/home/chli/chLi/Results/ma-sh/output/video/bunny_fit_1000x1000.mp4',
        fps=30,
        repeat_tag_list=[1],
        overwrite=False,
    )
    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh_render/bunny/anchor-50_1000x1000/mash/',
        '/home/chli/chLi/Results/ma-sh/output/video/bunny_fit_error_1000x1000.mp4',
        fps=30,
        repeat_tag_list=[1],
        overwrite=False,
    )
    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/render_crop/XiaomiSU7_1000x1000/anc-1500/',
        '/home/chli/chLi/Results/ma-sh/output/video/XiaomiSU7_crop_1000x1000.mp4',
        fps=30,
        repeat_tag_list=[1, -1],
        overwrite=True,
    )
    toVideo(
        '/home/chli/chLi/Results/ma-sh/output/render_crop/Washer_1000x1000/anc-1500/',
        '/home/chli/chLi/Results/ma-sh/output/video/Washer_crop_1000x1000.mp4',
        fps=30,
        repeat_tag_list=[-1, 1],
        overwrite=True,
    )
