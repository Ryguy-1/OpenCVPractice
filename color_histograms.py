from matplotlib import pyplot as plt
import numpy as np
import cv2

image_path = "dino.jpg"
cv2_image = cv2.imread(image_path)

print(cv2_image.shape)
cv2.imshow("Original", cv2_image)
cv2.waitKey(0)



# histogram = cv2.calcHist(cv2.split(cv2_image)[0], [0], None, [256], [0, 256])
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(histogram)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

chans = cv2.split(cv2_image)
# colors = ("b", "g", "r")
# plt.figure()
# plt.title("Color historgram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
#
# for (chan, color) in zip(chans, colors):
#     hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
#     plt.plot(hist, color=color)
#     plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print(f"2d histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

plt.show()


hist = cv2.calcHist([cv2_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print(f"3D histogram shape: {hist.shape}, with {hist.flatten().shape[0]}")

plt.show()

