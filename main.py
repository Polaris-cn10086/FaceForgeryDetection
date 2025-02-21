import config
from dataset import dataset

if __name__ == "__main__":
    print(config.work_dir)
    dataset.videos_to_images()
