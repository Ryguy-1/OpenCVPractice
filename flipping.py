import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)


flipped = cv2.flip(cv2_image, 1)
cv2.imshow("Horizontal Flip", flipped)
cv2.waitKey(0)

flipped = cv2.flip(cv2_image, 0)
cv2.imshow("Vertical Flip", flipped)
cv2.waitKey(0)

flipped = cv2.flip(cv2_image, -1)
cv2.imshow("Vertical and Horizontal Flip", flipped)
cv2.waitKey(0)
