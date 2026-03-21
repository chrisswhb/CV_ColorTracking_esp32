import cv2


def preprocess_frame(frame):
    """
    Light denoising before color detection.
    """
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    return hsv