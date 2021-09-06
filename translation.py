import numpy as np
import argparse
import imutils
import cv2

# Shape: y, then x
# Color: B, G, R

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)

# # translation
# shift_x = 200; shift_y = -100
# shift_matrix = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
# shifted_image = cv2.warpAffine(cv2_image, shift_matrix, (cv2_image.shape[1], cv2_image.shape[0])) # actually x, then y, but shape is weird
# cv2.imshow("Shifted Image", shifted_image)
# cv2.waitKey(0)
#
# # imutils translation
# shifted_image = imutils.translate(cv2_image, 500, 200)
# cv2.imshow("IMUTILS SHIFT", shifted_image)
# cv2.waitKey(0)

