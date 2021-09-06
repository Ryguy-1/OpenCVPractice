import numpy as np
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)

(B, G, R) = cv2.split(cv2_image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zero_place_holder = np.zeros(cv2_image.shape[:2], dtype="uint8")
cv2.imshow("Blue", cv2.merge([B, zero_place_holder, zero_place_holder]))
cv2.imshow("Green", cv2.merge([zero_place_holder, G, zero_place_holder]))
cv2.imshow("Red", cv2.merge([zero_place_holder, zero_place_holder, R]))
cv2.waitKey(0)

