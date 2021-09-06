import numpy as np
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)

gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
cv2.waitKey(0)