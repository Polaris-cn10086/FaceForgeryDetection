import string
import cv2
import os
import config


# 快速连接路径
def combine_path(path1: string, path2: string) -> string:
    return path1 + "/" + path2


# 将视频抽帧变为图片
# TODO 更快的速度
def videos_to_images():
    videos_path_list = os.listdir(config.videos_path)
    print(videos_path_list)

    for video_path in videos_path_list:
        cap = cv2.VideoCapture(combine_path(config.videos_path, video_path))
        print(combine_path(config.images_path, video_path))
        is_opened = cap.isOpened()
        image_num: int = 0
        image_sum: int = 0
        timef: int = 15
        print(is_opened)
        while is_opened:
            image_sum += 1
            (frame_state, frame) = cap.read()
            # 读不到了就推出
            if frame_state is False:
                break

            if image_sum % timef == 0:
                image_num += 1

                write_path = combine_path(
                    config.images_path, str(image_num) + ".jpg")

                print(write_path)

                cv2.imwrite(
                    write_path,
                    frame,
                    [cv2.IMWRITE_JPEG_CHROMA_QUALITY, 100],
                )
        print(str(image_num) + "all wirted")


# 加载数据集
def load_images_path() -> string:
    pass
