import numpy as np
import cv2 as cv
import random


def rand_tone():
    skintone = [random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)]

    image = cv.imread("img\\avatar_orig.png")
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Define lower and uppper limits of color
    lo_limit = np.array([0, 0, 0])
    hi_limit = np.array([10, 20, 150])

    # Mask image
    mask = cv.inRange(hsv, lo_limit, hi_limit)

    # Change image to skintone where we found color
    image[mask > 0] = skintone

    cv.imwrite("img\\avatar.png", image)

    return 'img\\avatar.png'


def add_mustache():
    img1 = cv.imread("img\\avatar.png")
    img2 = cv.imread("img\\mustache.png")

    # Coinvert from BGR to BGRA
    bgra = cv.cvtColor(img2, cv.COLOR_BGR2BGRA)

    # Slice of alpha channel
    alpha = bgra[:, :, 3]

    # Use logical indexing to set alpha channel to 0 where BGR=0
    alpha[np.all(bgra[:, :, 0:3] == (0, 0, 0), 2)] = 0
    result = cv.addWeighted(img1, 1, img2, 1, 0)

    cv.imwrite("img\\avatar_mustache.png", result)

    return 'img\\avatar_mustache.png'
