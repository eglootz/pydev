import cv2
import time


def picture(name):
    vc = cv2.VideoCapture(2)
    time.sleep(0.1)
    rval, frame = vc.read()
    cv2.imwrite(f"images/{name}.jpg", frame)
    cv2.destroyAllWindows()
    vc.release()

# if frame is not None:
# cv2.imshow("preview", frame)
#rval, frame = vc.read()

# if cv2.waitKey(1) & 0xFF == ord('q'):
#   break
