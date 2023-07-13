import numpy as np
from PIL import Image
import cv2

def imread(filename):
    return cv2.imread(filename)

def otsu(gaussian):
    return cv2.threshold(
        gaussian, 0., 255., cv2.THRESH_BINARY+cv2.THRESH_OTSU)


def edge_mask(img):
    gaussian = cv2.GaussianBlur(img, (9, 9), 0)
    edge =  cv2.adaptiveThreshold(gaussian, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    return edge


def combine(orig, masked_img):
    orig = orig.astype('uint8')
    masked_img = masked_img.astype('uint8')
    bilateral_img = cv2.bilateralFilter(orig, 9, 500, 500)
    print(bilateral_img.shape)
    print(masked_img.shape)
    return cv2.bitwise_and(bilateral_img, bilateral_img, mask=masked_img)


def cartoon_full(filename):
    image = cv2.cvtColor(imread(filename), cv2.COLOR_BGR2RGB)
    edges = edge_mask(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    return combine(image, edges)

# gaussian --> otsu --> noise (dilating and erosing) --> ... --> watershed