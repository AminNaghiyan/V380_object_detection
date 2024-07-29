from PIL import Image
import os

assets_path = 'assets/images'


def load_arrow_images():
    left_arrow_img = Image.open(os.path.join(assets_path, 'left_arrow.png'))
    right_arrow_img = Image.open(os.path.join(assets_path, 'right_arrow.png'))
    up_arrow_img = Image.open(os.path.join(assets_path, 'up_arrow.png'))
    down_arrow_img = Image.open(os.path.join(assets_path, 'down_arrow.png'))
    return left_arrow_img, right_arrow_img, up_arrow_img, down_arrow_img
