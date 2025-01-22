import os
import sys
import argparse
sys.path.append(os.getcwd())

from blender_manage.Method.check_pose import checkFilePose


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--shape_file_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--use_gpu",
        action='store_true',
    )

    argv = sys.argv[sys.argv.index("--") + 1 :]
    args = parser.parse_args(argv)

    checkFilePose(
        args.shape_file_path,
        args.use_gpu,
    )
