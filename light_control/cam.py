import cv2
import time


def picture(name):
    vc = cv2.VideoCapture(2)
    time.sleep(0.1)
    rval, frame = vc.read()
    cv2.imwrite(f"log_images/{name}.jpg", frame)
    cv2.destroyAllWindows()
    vc.release()
