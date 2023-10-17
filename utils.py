import cv2
import numpy as np


def img_pre_processing(img: np.ndarray) -> np.ndarray:
    img_blurred = cv2.GaussianBlur(img, (5, 5), 3)
    img_canny = cv2.Canny(img_blurred, 150, 200)
    return img_canny


def convert_to_bgr(image: np.ndarray) -> np.ndarray:
    if len(image.shape) == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image


def stack_images(*images: np.ndarray) -> np.ndarray:
    images_bgr = [convert_to_bgr(image) for image in images]
    return np.hstack(images_bgr)


