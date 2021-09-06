import numpy as np
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)

cropped_image = cv2_image[100:400, 200:500]
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)