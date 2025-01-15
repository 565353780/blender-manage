import os
import sys
import argparse
sys.path.append(os.getcwd())

from blender_manage.Method.render import renderFolder


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--shape_folder_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--save_image_folder_path",
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

    renderFolder(
        args.shape_folder_path,
        args.save_image_folder_path,
        args.use_gpu,
        args.overwrite)
