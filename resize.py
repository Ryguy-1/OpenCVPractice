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



# resize
new_height = 150
aspect_ratio = new_height/cv2_image.shape[1]
new_dimensions = (new_height, int(cv2_image.shape[0]*aspect_ratio))
resized_image = cv2.resize(cv2_image, new_dimensions, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)

# imutils resize
resized_image = imutils.resize(cv2_image, height=600)
cv2.imshow("Upside Down Image", resized_image)
cv2.waitKey(0)