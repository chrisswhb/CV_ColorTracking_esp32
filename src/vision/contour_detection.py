import cv2


def get_largest_contour(mask, min_area=500):
    """
    Returns the largest contour above a minimum area threshold.
    """
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return None

    largest = max(contours, key=cv2.contourArea)

    if cv2.contourArea(largest) < min_area:
        return None

    return largest


def get_bounding_box(contour):
    """
    Returns x, y, w, h for a contour.
    """
    return cv2.boundingRect(contour)