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



# rotation
(h, w) = cv2_image.shape[:2]
rotation_amount = 45
rotation_matrix = cv2.getRotationMatrix2D((w//2, h//2), rotation_amount, 1.0)  # center, rotation amount, scale
rotated_image = cv2.warpAffine(cv2_image, rotation_matrix, (cv2_image.shape[1], cv2_image.shape[0]))
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)

# imutils rotation
rotated_image = imutils.rotate(cv2_image, 180)
cv2.imshow("Upside Down Image", rotated_image)
cv2.waitKey(0)