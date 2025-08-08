BLENDER_VERSION=4.5
PYTHON_VERSION=3.11

if [ "$(uname)" = "Linux" ]; then
  sudo apt install libxkbcommon-x11-dev -y
fi

PYTHON_MACOS=/Applications/Blender.app/Contents/Resources/${BLENDER_VERSION}/python/bin/python${PYTHON_VERSION}
PYTHON_LINUX=$HOME/Install/blender/${BLENDER_VERSION}/python/bin/python${PYTHON_VERSION}

os_type=$(uname)

if [ "$os_type" = "Linux" ]; then
  PYTHON_BIN=${PYTHON_LINUX}
elif [ "$os_type" = "Darwin" ]; then
  PYTHON_BIN=${PYTHON_MACOS}
fi

${PYTHON_BIN} -m pip install pip --upgrade

${PYTHON_BIN} -m pip install open3d gradio-client opencv-python trimesh

pip install -U tqdm opencv-python numpy moviepy imageio imageio-ffmpeg
