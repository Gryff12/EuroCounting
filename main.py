import cv2
import numpy as np
from utils import *

def empty(a):
    pass
def main() -> None:
    # Capture vidéo depuis la caméra par défaut
    cap = cv2.VideoCapture(0)

    # Réglez la résolution de la caméra
    cap.set(3, 640)
    cap.set(4, 480)

    cv2.namedWindow("Settings")
    cv2.resizeWindow("Settings", 640,240)
    cv2.createTrackbar("Threshold1", "Settings", 50, 255, empty)
    cv2.createTrackbar("Threshold2", "Settings", 50, 255, empty)

    while True:
        success, image = cap.read()

        if success:
            processed_image = img_pre_processing(image)
            stacked_images = stack_images(image, processed_image)
            cv2.imshow('Euros', stacked_images)

            # Attendre 1 milliseconde et vérifier si l'utilisateur a appuyé sur la touche 'q' pour quitter
            key = cv2.waitKey(1) & 0xFF  # 0xFF to support all versions of OpenCV
            if key == ord('q'):
                break
        else:
            print("L'image n'a pas pu être chargée.")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
