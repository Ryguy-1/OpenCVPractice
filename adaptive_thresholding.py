import numpy as np
import cv2


cv2_image = cv2.imread("dino.jpg")
cv2.imshow("Original Image", cv2_image)
cv2.waitKey(0)

grayscale_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
gaussian_blur = cv2.GaussianBlur(grayscale_image, (21, 21), 0)
cv2.imshow("Gaussian Blur", gaussian_blur)

thresh = cv2.adaptiveThreshold(gaussian_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 5)
# cv2.imshow("Mean Threshold", thresh)
cv2.waitKey(0)

thresh2 = cv2.adaptiveThreshold(gaussian_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
# cv2.imshow("Gaussian Threshold", thresh2)
cv2.waitKey(0)

combined = np.hstack([
    thresh,
    thresh2
])
cv2.imshow("Mean, Gaussian", combined)
# cv2.waitKey(0)

