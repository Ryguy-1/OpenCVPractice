import numpy as np
import cv2

cv2_image = cv2.imread("dino.jpg")
cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", cv2_image)
cv2.waitKey(0)

blurred_image = cv2.GaussianBlur(cv2_image, (21, 21), 0)
cv2.imshow("Gaussian Blurred Img", blurred_image)
cv2.waitKey(0)

(T, thresh) = cv2.threshold(blurred_image, 135, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)

(T, thresh) = cv2.threshold(blurred_image, 135, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverted", thresh)
cv2.waitKey(0)

cv2.imshow("Dino", cv2.bitwise_and(cv2_image, cv2_image, mask=thresh))
cv2.waitKey(0)