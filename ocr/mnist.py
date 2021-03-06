import pickle
import numpy as np
from PIL import Image
from resizeimage import resizeimage
from ocr.settings import *


def ask_img():
    return input("Enter the image name: ")


def resize_img(img_name):
    with open(img_name, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [28, 28])
            cover.save(img_name, image.format)
            return cover, image


def load_model(path):
    model = pickle.load(open(path, 'rb'))
    return model


def main():
    img_name = ask_img()
    model = load_model()
    cover, image = resize_img(img_name)
    cover.save(img_name, image.format)

    img_arr = np.array(cover)
    img_reshaped = img_arr.reshape(1, -1)
    number = model.predict(img_reshaped)
    print(number)

