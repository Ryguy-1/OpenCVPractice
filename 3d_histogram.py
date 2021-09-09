from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2

cv2_image = cv2.imread("dino.jpg")
size = 5000
bins = 8

hist = cv2.calcHist([cv2_image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])

print(f"3D histogram shape: {hist.shape} with {hist.flatten().shape[0]} values")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ratio = size / np.max(hist)

for (x, plane) in enumerate(hist):
    for (y, row) in enumerate(plane):
        for (z, col) in enumerate(row):
            if hist[x][y][z] > 0.0:
                siz = ratio * hist[x][y][z]
                rgb = (z / (bins -1), y / (bins - 1), x /(bins - 1))
                ax.scatter(x, y, z, s=siz, facecolors=rgb)

plt.show()
