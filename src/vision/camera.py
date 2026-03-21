import cv2


def initialize_camera(width=640, height=480):

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    return cap


def get_frame(cap):

    ret, frame = cap.read()

    if not ret:
        return None

    return frame


def release_camera(cap):

    cap.release()
    cv2.destroyAllWindows()