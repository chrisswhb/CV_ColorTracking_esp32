import cv2
from src.vision.camera import initialize_camera, get_frame, release_camera
from src.vision.preprocessing import preprocess_frame
from src.vision.color_detection import get_red_mask, get_green_mask, clean_mask
from src.vision.contour_detection import get_largest_contour, get_bounding_box
from src.vision.tracker import get_object_center, get_horizontal_direction


def main():
    cap = initialize_camera()

    while True:
        frame = get_frame(cap)
        if frame is None:
            break

        hsv = preprocess_frame(frame)

        red_mask = clean_mask(get_red_mask(hsv))
        green_mask = clean_mask(get_green_mask(hsv))

        red_contour = get_largest_contour(red_mask)
        green_contour = get_largest_contour(green_mask)

        display = frame.copy()
        frame_width = display.shape[1]

        if red_contour is not None:
            x, y, w, h = get_bounding_box(red_contour)
            cx, cy = get_object_center(x, y, w, h)
            direction = get_horizontal_direction(cx, frame_width)

            cv2.rectangle(display, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.circle(display, (cx, cy), 5, (255, 0, 0), -1)
            cv2.putText(display, f"RED - {direction}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if green_contour is not None:
            x, y, w, h = get_bounding_box(green_contour)
            cx, cy = get_object_center(x, y, w, h)

            cv2.rectangle(display, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(display, (cx, cy), 5, (255, 0, 0), -1)
            cv2.putText(display, "GREEN", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.line(display, (frame_width // 2, 0), (frame_width // 2, display.shape[0]), (255, 255, 255), 1)

        cv2.imshow("Detection", display)
        cv2.imshow("Red Mask", red_mask)
        cv2.imshow("Green Mask", green_mask)

        if cv2.waitKey(1) == 27:
            break

    release_camera(cap)


if __name__ == "__main__":
    main()