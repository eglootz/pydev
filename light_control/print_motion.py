# a program to check for motion while it is running and send out "true" or "false"
# every second, while using the function from check_motion to check for motion

from check_motion import check_motion
import time

while True:
    time.sleep(1)
    print(f"Motion: {check_motion()}")
