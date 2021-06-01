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
