import numpy as np
import cv2

def translate(img, x, y):
    shift_matrix = np.float32([[1, 0, x], [0, 1, y]])
    shifted_image = cv2.warpAffine(img, shift_matrix, (img.shape[1], img.shape[0]))
    return shifted_image

def rotate(img, deg):
    shift_matrix = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), deg, 1.0)
    rotated_image = cv2.warpAffine(img, shift_matrix, (img.shape[1], img.shape[0]))
    return rotated_image

def resize(img, width=None, height=None, inter=cv2.INTER_AREA):
    new_dimensions = None
    (h, w) = img.shape[:2]
    if width is None and height is None:
        return img
    elif height is None:
        aspect_ratio = width/float(w)
        new_dimensions = (width, int(h*aspect_ratio))
    elif width is None:
        aspect_ratio = height/float(h)
        new_dimensions = (int(w*aspect_ratio), height)

    try:
        return cv2.resize(img, new_dimensions, interpolation=inter)
    except Exception:
        print("Error Resizing Image")
        print(Exception)
        quit()
