from check_motion import check_motion
import time

while True:
    time.sleep(1)
    print(f"Motion: {check_motion()}")
