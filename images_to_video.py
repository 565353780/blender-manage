from blender_manage.Method.video import toVideo, toGif


def toBunnyFitVideo():
    for anchor_num in [10, 20, 50, 100, 200, 400]:
        toVideo(
            '/home/chli/chLi/Results/ma-sh/output/render/bunny-' + str(anchor_num) + 'anc_1000x1000/',
            '/home/chli/chLi/Results/ma-sh/output/video/bunny-' + str(anchor_num) + 'anc_1000x1000.mp4',
            fps=90,
            repeat_tag_list=[1],
            overwrite=True,
        )
    return

def toBunnyFitErrorVideo():
    for anchor_num in [10, 20, 50, 100, 200, 400]:
        toVideo(
            '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh_render/bunny/anchor-' + str(anchor_num) + '_1000x1000/mash/',
            '/home/chli/chLi/Results/ma-sh/output/video/bunny_' + str(anchor_num) + 'anc_error_1000x1000.mp4',
            fps=90,
            repeat_tag_list=[1],
            overwrite=True,
        )
    return

def toCropVideo():
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
    return

def toThingi10KGif():
    toGif(
        '/home/chli/chLi/Results/3DShape2VecSet/render/Thingi10K-46602_1000x1000/Thingi10K-46602/',
        '/home/chli/chLi/Results/3DShape2VecSet/video/Thingi10K-46602_1000x1000.gif',
        fps=10,
        repeat_tag_list=[1],
        overwrite=True,
    )
    toGif(
        '/home/chli/chLi/Results/3DShape2VecSet/render/Thingi10K-61258_1000x1000/Thingi10K-61258/',
        '/home/chli/chLi/Results/3DShape2VecSet/video/Thingi10K-61258_1000x1000.gif',
        fps=10,
        repeat_tag_list=[1],
        overwrite=True,
    )

    return

if __name__ == '__main__':
    # toBunnyFitVideo()
    # toBunnyFitErrorVideo()
    # toCropVideo()
    toThingi10KGif()
