import numpy as np
import cv2
import mahotas


cv2_image = cv2.imread("dino.jpg")
cv2.imshow("Original Image", cv2_image)
cv2.waitKey(0)
cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(cv2_image, cv2.CV_64F)  # Need to use 64 bit float
laplacian = np.uint8(np.absolute(laplacian))  # This process (this line and the last) ensures you don't miss edges.
cv2.imshow("Laplacian", laplacian)
cv2.waitKey(0)


sobelX = cv2.Sobel(cv2_image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(cv2_image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(sobelX)
sobelY = np.uint8(sobelY)

sobel_combined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("Sobel X", sobelY)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Combined SOBELX and SOBELY", sobel_combined)
cv2.waitKey(0)


