# importing other files and functions from this directory
import light_control as lc
import check_motion as cm
# importing urllib3 for disabling warnings
import urllib3
# importing the time module for logging motion times
import time
# import the camera function
import cam


current_motion = False

while True:
    motion = cm.check_motion()

    if motion == True and current_motion == False:
        current_time = time.strftime('%H:%M:%S')
        print(f"Motion detected: {current_time}")
        lc.red_light()
        cam.picture(name=f"{current_time}")
        current_motion = True
    if motion == False:
        current_motion = False
        lc.white_light()
