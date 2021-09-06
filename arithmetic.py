import numpy as np
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)

print(f"Max of 255: {cv2.add(np.uint8([200]), np.uint8([100]))}")
print(f"Min of 0: {cv2.subtract(np.uint8([50]), np.uint8([100]))}")

print(f"Wrap Around: {(np.uint8([200])+np.uint8([100]))}")
print(f"Wrap Around: {(np.uint8([50])-np.uint8([100]))}")

adding_matrix = np.ones(cv2_image.shape, dtype='uint8') * 100
added_image = cv2.add(cv2_image, adding_matrix)
cv2.imshow("Added Image CV2", added_image)
cv2.waitKey(0)

subtracting_matrix = np.ones(cv2_image.shape, dtype='uint8')*50
subtracted_image = cv2.subtract(cv2_image, subtracting_matrix)
cv2.imshow("Subtracted Image", subtracted_image)
cv2.waitKey(0)


