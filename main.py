import cv2
from src.vision.camera import initialize_camera, get_frame, release_camera


def main():

    cap = initialize_camera()

    while True:

        frame = get_frame(cap)

        if frame is None:
            break

        cv2.imshow("Camera Feed", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    release_camera(cap)


if __name__ == "__main__":
    main()