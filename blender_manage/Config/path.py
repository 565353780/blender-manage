import os

GIT_ROOT_FOLDER_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../../')

if GIT_ROOT_FOLDER_PATH[-1] != '/':
    GIT_ROOT_FOLDER_PATH += '/'

BLENDER_BIN_MACOS = '/Applications/Blender.app/Contents/MacOS/Blender'
BLENDER_BIN_LINUX = os.environ['HOME'] + '/Install/blender/blender'

BLENDER_BIN = None
if os.path.exists(BLENDER_BIN_MACOS):
    BLENDER_BIN = BLENDER_BIN_MACOS
elif os.path.exists(BLENDER_BIN_LINUX):
    BLENDER_BIN = BLENDER_BIN_LINUX
