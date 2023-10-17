import cv2
import numpy as np
from utils import *


def main():
    image_path = 'images/test_image.jpg'
    image = cv2.imread(image_path)

    if image is not None:
        processed_image = img_pre_processing(image)
        stacked_images = stack_images(image, processed_image)

        # Affichez l'image superposée dans une fenêtre spécifiée
        cv2.imshow('Euros', stacked_images)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("L'image n'a pas pu être chargée.")


if __name__ == "__main__":
    main()
