import os
import re
import cv2
import imageio
import numpy as np
from tqdm import tqdm
from moviepy import ImageSequenceClip


def extract_numbers(filename):
    return [int(num) for num in re.findall(r'\d+', filename)]

def sort_filenames(filenames):
    return sorted(filenames, key=extract_numbers)

def getSortedImageFileNameList(
    image_folder_path: str,
    valid_format_list: list = ['.png', '.jpg', '.jpeg'],
) -> list:
    if not os.path.exists(image_folder_path):
        print('[ERROR][video::getSortedImageFileNameList]')
        print('\t image folder not exist!')
        print('\t image_folder_path:', image_folder_path)
        return []

    if len(valid_format_list) == 0:
        print('[ERROR][video::getSortedImageFileNameList]')
        print('\t format not defined!')
        return []

    image_file_name_list = os.listdir(image_folder_path)

    valid_image_file_name_list = []
    for image_file_name in image_file_name_list:
        if '.' + image_file_name.split('.')[-1] not in valid_format_list:
            continue

        valid_image_file_name_list.append(image_file_name)

    sorted_valid_image_file_name_list = sort_filenames(valid_image_file_name_list)

    return sorted_valid_image_file_name_list

def getSortedImageFilePathList(
    image_folder_path: str,
    valid_format_list: list = ['.png', '.jpg', '.jpeg'],
) -> list:
    sorted_image_file_name_list = getSortedImageFileNameList(image_folder_path, valid_format_list)

    sorted_valid_image_file_path_list = [
        image_folder_path + image_file_name for image_file_name in sorted_image_file_name_list
    ]

    return sorted_valid_image_file_path_list

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

    image_files = getSortedImageFilePathList(image_folder_path)

    frame = cv2.imread(image_files[0], cv2.IMREAD_UNCHANGED)
    if frame.dtype == np.uint16:
        frame = (frame / 256).astype('uint8')

    if frame.shape[-1] == 4:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    height, width = frame.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(save_video_file_path, fourcc, fps, (width, height))

    print('[INFO][image_to_video::toVideo]')
    print('\t start convert images to video...')
    for img_file in tqdm(image_files):
        img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
        if img.dtype == np.uint16:
            img = (img / 256).astype('uint8')

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

    image_files = getSortedImageFilePathList(image_folder_path)

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

    image_files = getSortedImageFilePathList(image_folder_path)

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
