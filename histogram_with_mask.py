from matplotlib import pyplot as plt
import numpy as np
import cv2


def main():
    cv2_image = cv2.imread("dino.jpg")
    cv2.imshow("Original", cv2_image)
    cv2.waitKey(0)
    # plot_histogram(cv2_image, "Histogram for OG Image")

    mask = np.zeros((cv2_image.shape[0], cv2_image.shape[1]), dtype="uint8")
    # rect_start = (cv2_image.shape[0]/4, cv2_image.shape[1]/4)
    # rect_end = (cv2_image.shape[0]*3/4, cv2_image.shape[1]*3/4)
    # print(rect_start)
    # print("=========")
    # print(rect_end)
    # print(mask.shape)
    # cv2.rectangle(mask, rect_start, rect_end, 255, -1)
    cv2.rectangle(mask, (15, 15), (500, 300), 255, -1)
    cv2.imshow("Mask", mask)
    cv2.waitKey(0)

    masked_image = cv2.bitwise_and(cv2_image, cv2_image, mask=mask)
    cv2.imshow("Mask Applied", masked_image)
    cv2.waitKey(0)
    plot_histogram(cv2_image, "Histogram for masked Image", mask=mask)
    plt.show()

def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    # plt.show()



if __name__ == '__main__':
    main()