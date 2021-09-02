from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="dino.jpg")
args = vars(ap.parse_args())  # Args becomes a dictionary
image = cv2.imread(args['image'])  # reads it from the command line input

print(f"width: {image.shape[1]} pixels")
print(f"height: {image.shape[0]} pixels")
print(f"channels: {image.shape[2]}")

cv2.imshow("Image", image)  #
cv2.waitKey(0)


