import numpy as np
import cv2

rectangle_canvas = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle_canvas, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle_canvas)
cv2.waitKey(0)

circle_canvas = np.zeros((300, 300), dtype="uint8")
print((circle_canvas.shape[1]//2, circle_canvas.shape[0]//2))
print((circle_canvas.shape[0]-20))
cv2.circle(circle_canvas, (circle_canvas.shape[1]//2, circle_canvas.shape[0]//2), (circle_canvas.shape[0]-20)//2, 255, -1)
cv2.imshow("Circle", circle_canvas)
cv2.waitKey(0)

bitwise_and = cv2.bitwise_and(rectangle_canvas, circle_canvas)
cv2.imshow("bitwise_and", bitwise_and)
cv2.waitKey(0)

bitwise_or = cv2.bitwise_or(rectangle_canvas, circle_canvas)
cv2.imshow("bitwise_or", bitwise_or)
cv2.waitKey(0)

bitwise_x_or = cv2.bitwise_xor(rectangle_canvas, circle_canvas)
cv2.imshow("bitwise_x_or", bitwise_x_or)
cv2.waitKey(0)

bitwise_not = cv2.bitwise_not(circle_canvas)
cv2.imshow("bitwise_not", bitwise_not)
cv2.waitKey(0)

