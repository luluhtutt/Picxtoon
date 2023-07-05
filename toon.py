import numpy as np
from PIL import Image
import cv2

# Read and convert a colored image into a floating point array with values between 0 and 1.


def imread(filename):
    image = Image.open(filename)
    image_rgb = image.convert('RGB')
    image_data = np.asarray(image_rgb, dtype='uint8')
    return image_data / 255.


def imread_gray(filename):
    return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)


def gray_scale(img):
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = 0.2125*img[:, :, 0] + 0.7154*img[:, :, 1] + 0.0721*img[:, :, 2]
    # img_gray = img.convert('L')
    return img_gray


def gaussianizing(img):
    return cv2.GaussianBlur(img, (9, 9), 0)


def edge_mask(gaussian):
    return cv2.adaptiveThreshold(gaussian, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)


def otsu(gaussian):
    return cv2.threshold(
        gaussian, 0., 255., cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# gaussian --> otsu --> noise (dilating and erosing) --> ... --> watershed
