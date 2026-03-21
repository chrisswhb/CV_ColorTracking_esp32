def get_object_center(x, y, w, h):
    cx = x + w // 2
    cy = y + h // 2
    return cx, cy


def get_horizontal_direction(cx, frame_width, tolerance=40):
    frame_center = frame_width // 2

    if cx < frame_center - tolerance:
        return "LEFT"
    if cx > frame_center + tolerance:
        return "RIGHT"
    return "CENTER"