# importing other files and functions from this directory
import light_control as lc
import check_motion as cm
import cam
# importing the time module for logging motion times
import time

# set current_motion to false to start the program
current_motion = False

while True:
    motion = cm.check_motion()

    if motion == True and current_motion == False:
        current_time = time.strftime('%H:%M:%S')
        print(f"Motion detected: {current_time}")
        lc.light("red")
        cam.picture(name=current_time)
        current_motion = True
    if motion == False:
        current_motion = False
        lc.light("white")
