BLENDER_BIN_MACOS=/Applications/Blender.app/Contents/MacOS/Blender
BLENDER_BIN_LINUX=$HOME/Install/blender/blender

os_type=$(uname)

if [ "$os_type" = "Linux" ]; then
  BLENDER_BIN=${BLENDER_BIN_LINUX}
elif [ "$os_type" = "Darwin" ]; then
  BLENDER_BIN=${BLENDER_BIN_MACOS}
fi

pkill -f "$BLENDER_BIN"

pkill -f "blender"
