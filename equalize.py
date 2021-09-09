from matplotlib import pyplot as plt
import numpy as np
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)


grayscaled_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(grayscaled_image)
cv2.imshow("Grayscale Image", grayscaled_image)
cv2.imshow("Equalized Image", equalized_image)
cv2.waitKey(0)

