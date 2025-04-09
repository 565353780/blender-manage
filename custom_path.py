data_dict = {}
for anchor_num in [10, 20, 50, 100, 200, 400]:
    tag = str(anchor_num)
    data_dict['bunny-' + tag + 'anc'] = [
        '/home/chli/chLi/Results/ma-sh/output/fit/fixed/bunny/anchor-' + tag + '/pcd/',
        '/home/chli/chLi/Results/ma-sh/output/render/bunny-' + tag + 'anc_1000x1000/',
    ]

    data_dict['bunny-' + tag + 'anc_error'] = [
        '/home/chli/chLi/Results/ma-sh/output/fit_error_mesh/bunny/anchor-' + tag + '/mash/',
        '/home/chli/chLi/Results/ma-sh/output/render/bunny-' + tag + 'anc_1000x1000/',
    ]


    data_dict['chair-' + tag + 'anc'] = [
        '/home/chli/chLi/Results/ma-sh/output/fit/fixed/03001627_e71d05f223d527a5f91663a74ccd2338/anchor-' + tag + '/pcd/',
        '/home/chli/chLi/Results/ma-sh/output/render/chair-' + tag + 'anc_1000x1000/',
    ]

for model_id in [46602, 61258]:
    tag = str(model_id)
    data_dict['Thingi10K-' + tag] = [
        '/home/chli/github/ASDF/td-shape-to-vec-set/output/auto_encoder/kl_d512_m512_l8_d24_edm/Thingi10K-' + tag + '.obj',
        '/home/chli/chLi/Results/3DShape2VecSet/render/Thingi10K-' + tag + '_1000x1000/',
    ]

bunny_fit_shape_id_list = [
    'bunny-10anc',
    'bunny-20anc',
    'bunny-50anc',
    'bunny-100anc',
    'bunny-200anc',
    'bunny-400anc',
]

bunny_fit_error_shape_id_list = [
    'bunny-10anc_error',
    'bunny-20anc_error',
    'bunny-50anc_error',
    'bunny-100anc_error',
    'bunny-200anc_error',
    'bunny-400anc_error',
]

chair_fit_shape_id_list = [
    'chair-10anc',
    'chair-20anc',
    'chair-50anc',
    'chair-100anc',
    'chair-200anc',
    'chair-400anc',
]

thingi10k_fit_shape_id_list = [
    'Thingi10K-46602',
    'Thingi10K-61258',
]
