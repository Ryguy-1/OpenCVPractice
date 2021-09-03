import numpy as np
import cv2

# canvas = np.zeros((800, 800, 3), dtype='uint8')  # need to use uint8 because color is 8 bit
# print(canvas.shape)
#
# green = (0, 255, 0)  # b, g, r
# cv2.line(canvas, (0, 0), (800, 800), green, 8)
# print(canvas)
#
#
# blue = (255, 0, 0)
# cv2.rectangle(canvas, (100, 100), (500, 300), blue, -1)
# cv2.imshow("Custom Canvas2", canvas)
# cv2.waitKey(0)
#
#
# # Note: // = floor division for ints -> no rounding errors
# canvas2 = np.zeros((800, 800, 3), dtype='uint8')
# (center_x, canter_y) = (canvas.shape[1]//2, canvas.shape[0]//2)
# green = (0, 255, 0)
# print(canvas.shape[0])
# for r in range(0, canvas2.shape[0]//2, 50):
#     cv2.circle(canvas2, (center_x, canter_y), r, green, 5)
#
# cv2.imshow("Canvas3", canvas2)
# cv2.waitKey(0)



canvas = np.zeros((800, 800, 3), dtype='uint8')
for i in range(0, 30):
    radius = np.random.randint(10, high=100)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=800, size=(2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas Circles Random", canvas)
cv2.waitKey(0)