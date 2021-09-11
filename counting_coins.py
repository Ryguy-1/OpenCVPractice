import numpy as np
import cv2
import imutils

image = cv2.imread("coins2.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = image[:image.shape[0]:, :image.shape[1]]  # for easy rescaling later

image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred Image", image)
cv2.waitKey(0)

edged = cv2.Canny(image, 70, 90)
cv2.imshow("Canny", edged)
cv2.waitKey(0)

(contours, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"I count {len(contours)} coins in this image")
coins = image.copy()
cv2.drawContours(coins, contours, -1, (0, 255, 0), 2)  # -1 = draw all contours -> otherwise, it's the index
cv2.imshow("Coins", coins)
cv2.waitKey(0)

for (i, c) in enumerate(contours):
    (x, y, w, h) = cv2.boundingRect(c)
    print(f"Coin #{i+1}")
    coin = image[y:y+h, x:x+w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(image.shape[:2], dtype = 'uint8')
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)


# Another example
contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)