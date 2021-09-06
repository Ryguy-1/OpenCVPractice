import numpy as np
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)


mask = np.zeros(cv2_image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (int(mask.shape[1]*1/4), int(mask.shape[0]*1/4)), (int(mask.shape[1]*3/4), int(mask.shape[0]*3/4)), 255, -1)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

masked_image = cv2.bitwise_and(cv2_image, cv2_image, mask=mask)
cv2.imshow("Masked Image", masked_image)
cv2.waitKey(0)