import numpy as np
import cv2

cv2_image = cv2.imread("dino.jpg")
cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
cv2_image = cv2.GaussianBlur(cv2_image, (11, 11), 0)

canny_image = cv2.Canny(cv2_image, 30, 150)
cv2.imshow("Canny Image", canny_image)
cv2.waitKey(0)