import cv2
import numpy as np
import numpy.typing as npt


def sharpen_apply(frame: npt.NDArray, value) -> npt.NDArray:
    """
    Apply a sharpen filter. Enhances details.
    :param frame: frame to filter
    :param value: slider value
    :return: filtered frame
    """
    if value > 0:
        kernel = np.array([[0, -1, 0], [-1, 5 + value, -1], [0, -1, 0]])
        frame = cv2.filter2D(frame, -1, kernel)
    return frame
