import numpy as np
import cv2
import mahotas


cv2_image = cv2.imread("dino.jpg")
cv2.imshow("Original Image", cv2_image)
cv2.waitKey(0)

grayscale_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
gaussian_blur = cv2.GaussianBlur(grayscale_image, (21, 21), 0)
cv2.imshow("Gaussian Blur", gaussian_blur)

T = mahotas.thresholding.otsu(gaussian_blur)
print(f"Otsu's Threshold: {T}")
thresh = grayscale_image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)

T = mahotas.thresholding.rc(gaussian_blur)
print(f"Riddler-Calvard: {T}")
thresh = grayscale_image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)