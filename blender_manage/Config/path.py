import os

BLENDER_BIN_MACOS = '/Applications/Blender.app/Contents/MacOS/Blender'
BLENDER_BIN_LINUX = os.environ['HOME'] + '/Install/blender/blender'

BLENDER_BIN = None
if os.path.exists(BLENDER_BIN_MACOS):
    BLENDER_BIN = BLENDER_BIN_MACOS
elif os.path.exists(BLENDER_BIN_LINUX):
    BLENDER_BIN = BLENDER_BIN_LINUX
