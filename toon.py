import numpy as np
from PIL import Image
import cv2

# Read and convert a colored image into a floating point array with values between 0 and 1.


def imread(filename):
    image = Image.open(filename)
    image_rgb = image.convert('RGB')
    image_data = np.asarray(image_rgb)
    return image_data / 255.


# def gray_scale(img):
#     # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # img_gray = 0.2125*img[:, :, 0] + 0.7154*img[:, :, 1] + 0.0721*img[:, :, 2]
#     # img_gray = img.convert('L')
#     return img_gray


# def gaussianizing(image):

    # gaussian --> otzu --> noise (dilating and erosing) --> ... --> watershed
