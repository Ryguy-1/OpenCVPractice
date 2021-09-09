import numpy as np
import cv2

cv2_image = cv2.imread("dino.jpg")
cv2.imshow("Original Image", cv2_image)
cv2.waitKey(0)

blurred_image = np.hstack([  # creates 1 image of 3 side by side -> concatenates the arrays basically
    # cv2.blur(cv2_image, (3, 3)),
    cv2.blur(cv2_image, (3, 3)),
    cv2.blur(cv2_image, (7, 7)),
])
cv2.imshow("Averaged Image", blurred_image)
cv2.waitKey(0)

gaussian_blur = np.hstack([
    cv2.GaussianBlur(cv2_image, (3, 3), 0),  # the 0 is standard deviation -> 0 tells cv2 to compute it automatically based on kernel size
    cv2.GaussianBlur(cv2_image, (7, 7), 0)
])
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.waitKey(0)

# MEDIAN BLUR -> REDUCE NOISE!! -> median blur is actually OP

median_blur = np.hstack([
    cv2.medianBlur(cv2_image, 7),
    cv2.medianBlur(cv2_image, 21)
])
cv2.imshow("Median Blur", median_blur)
cv2.waitKey(0)


bilateral_blurring = np.hstack([
    cv2.bilateralFilter(cv2_image, 5, 21, 21),
    cv2.bilateralFilter(cv2_image, 9, 41, 41)
])
cv2.imshow("Bilateral", bilateral_blurring)
cv2.waitKey(0)