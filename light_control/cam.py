import cv2
import time


def initialize():
    vc = cv2.VideoCapture(2)


def picture(name):
    vc = cv2.VideoCapture(2)
    # waiting a short moment because else the picture would be dark
    time.sleep(0.1)
    rval, frame = vc.read()
    cv2.imwrite(f"log_images/{name}.jpg", frame)
