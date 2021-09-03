from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', "--image", required=True, help="")  # '-i' = input key, '--image' = storage in dictionary
args = vars(ap.parse_args())  # Args becomes a dictionary
image = cv2.imread(args['image'])  # reads it from the command line input

print(f"width: {image.shape[1]} pixels")
print(f"height: {image.shape[0]} pixels")
print(f"channels: {image.shape[2]}")

cv2.imshow("Image", image)  # image frame title, read_image
cv2.waitKey(0)  # any keypress will up-pause execution
cv2.imwrite("dino2.jpg", image)  # write the new image

print(image.shape)  # Height, then width, then channels

(b, g, r) = image[0, 0]  # BACKWARDS???
print(f'Pixel 0, 0 r, g, b values are {r, b, g}')

image[0, 0] = (0, 0, 255)  # Set the image at 0, 0 to new rgb values. -> red value of 255

print(image[0, 0])  # Check to make sure it worked -> it did lol

# crop image
cropped_corner = image[0:500, 0:500]
cv2.imshow("cropped image", cropped_corner)
cv2.waitKey(0)

