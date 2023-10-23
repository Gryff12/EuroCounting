import cv2
import numpy as np


def img_pre_processing(img: np.ndarray) -> np.ndarray:
    img_blurred = cv2.GaussianBlur(img, (5, 5), 3)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Settings")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Settings")
    img_canny = cv2.Canny(img_blurred, threshold1, threshold2)

    kernel = np.ones((3, 3), np.uint8)

    img_dilated = cv2.dilate(img_canny, kernel, iterations=1)
    img_pre = cv2.morphologyEx(img_dilated,cv2.MORPH_CLOSE, kernel)
    return img_pre


def convert_to_bgr(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image


def stack_images(*images: np.ndarray) -> np.ndarray:
    images_bgr = [convert_to_bgr(image) for image in images]
    return np.hstack(images_bgr)
