from matplotlib import pyplot as plt
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)

img_grayscale = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", img_grayscale)
cv2.waitKey(0)

histogram = cv2.calcHist(img_grayscale, [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(histogram)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

