import os
import sys
import argparse
sys.path.append(os.getcwd())

from blender_manage.Method.render_around_objaverse import renderAroundObjaverseFile


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--shape_file_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--render_image_num",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--save_image_file_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--use_gpu",
        action='store_true',
    )
    parser.add_argument(
        "--overwrite",
        action='store_true',
    )

    argv = sys.argv[sys.argv.index("--") + 1 :]
    args = parser.parse_args(argv)

    renderAroundObjaverseFile(
        args.shape_file_path,
        args.render_image_num,
        args.save_image_file_path,
        args.use_gpu,
        args.overwrite)
