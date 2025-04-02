import os
import cv2
import glob
import imageio
import numpy as np
from tqdm import tqdm
from moviepy import ImageSequenceClip


def toVideo(
    image_folder_path: str,
    save_video_file_path: str,
    fps: int = 30,
    overwrite: bool = False,
) -> bool:
    if os.path.exists(save_video_file_path):
        if not overwrite:
            return True

        os.remove(save_video_file_path)

    save_video_file_name = save_video_file_path.split('/')[-1]
    save_video_folder_path = save_video_file_path[:-len(save_video_file_name)]
    os.makedirs(save_video_folder_path, exist_ok=True)

    image_files = sorted(
        glob.glob(os.path.join(image_folder_path, "*.jpg")) +
        glob.glob(os.path.join(image_folder_path, "*.jpeg")) +
        glob.glob(os.path.join(image_folder_path, "*.png")),
        key=lambda x: int(os.path.basename(x).split('.')[0])
    )

    frame = cv2.imread(image_files[0], cv2.IMREAD_UNCHANGED)
    if frame.shape[-1] == 4:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    height, width = frame.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(save_video_file_path, fourcc, fps, (width, height))

    print('[INFO][image_to_video::toVideo]')
    print('\t start convert images to video...')
    for img_file in tqdm(image_files):
        img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)

        if img.shape[-1] == 4:
            alpha_channel = img[:, :, 3]
            img = img[:, :, :3]

            white_background = np.ones_like(img, dtype=np.uint8) * 255

            alpha_factor = alpha_channel[:, :, np.newaxis] / 255.0
            img = img * alpha_factor + white_background * (1 - alpha_factor)
            img = img.astype(np.uint8)

        video.write(img)

    video.release()
    cv2.destroyAllWindows()
    return True

def toAvi(
    image_folder_path: str,
    save_video_file_path: str,
    fps: int = 30,
    overwrite: bool = False,
) -> bool:
    if os.path.exists(save_video_file_path):
        if not overwrite:
            return True

        os.remove(save_video_file_path)

    save_video_file_name = save_video_file_path.split('/')[-1]
    save_video_folder_path = save_video_file_path[:-len(save_video_file_name)]
    os.makedirs(save_video_folder_path, exist_ok=True)

    image_files = sorted(
        glob.glob(os.path.join(image_folder_path, "*.jpg")) +
        glob.glob(os.path.join(image_folder_path, "*.jpeg")) +
        glob.glob(os.path.join(image_folder_path, "*.png")),
        key=lambda x: int(os.path.basename(x).split('.')[0])
    )

    clip = ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(save_video_file_path, codec="png", fps=fps)
    return True

def toGif(
    image_folder_path: str,
    save_video_file_path: str,
    fps: int = 30,
    overwrite: bool = False,
) -> bool:
    if os.path.exists(save_video_file_path):
        if not overwrite:
            return True

        os.remove(save_video_file_path)

    save_video_file_name = save_video_file_path.split('/')[-1]
    save_video_folder_path = save_video_file_path[:-len(save_video_file_name)]
    os.makedirs(save_video_folder_path, exist_ok=True)

    image_files = sorted(
        glob.glob(os.path.join(image_folder_path, "*.jpg")) +
        glob.glob(os.path.join(image_folder_path, "*.jpeg")) +
        glob.glob(os.path.join(image_folder_path, "*.png")),
        key=lambda x: int(os.path.basename(x).split('.')[0])
    )

    images = []
    for f in image_files:
        img = imageio.imread(f)
        images.append(img)

    imageio.mimsave(
        save_video_file_path,
        images,
        format='GIF',
        duration=1000/fps,
        loop=0,
        disposal=2,
    )
    return True
