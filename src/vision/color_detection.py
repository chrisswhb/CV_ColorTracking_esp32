import cv2
import numpy as np


def get_red_mask(hsv):
    """
    Red wraps around the HSV hue axis, so we use two ranges.
    """
    lower_red_1 = np.array([0, 120, 70])
    upper_red_1 = np.array([10, 255, 255])

    lower_red_2 = np.array([170, 120, 70])
    upper_red_2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)

    return cv2.bitwise_or(mask1, mask2)


def get_green_mask(hsv):
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([85, 255, 255])

    return cv2.inRange(hsv, lower_green, upper_green)


def clean_mask(mask):
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask