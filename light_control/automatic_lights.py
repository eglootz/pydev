# importing other files and functions from this directory
import light_control as lc
import check_motion as cm
import cam
import send_mail as sm
# importing the time module for logging motion times
import time
import tweet as t
import os

print("Starting the program...")

# set current_motion to false to start the program
current_motion = False

while True:
    # time.sleep(20)
    motion = cm.check_motion()

    if motion == True and current_motion == False:
        current_time = time.strftime('%H:%M:%S')
        print(f"Motion detected: {current_time}")
        lc.light("red")
        cam.picture(name=current_time)
        current_motion = True

        alert = f"Motion detected at {current_time}!"
        # mail stuff

        content = f"There was a motion in your room - who could it be? ({current_time})"
        sm.send_mail(subject=alert, content=content,
                     person="Bewegungslogger")
        print("Mail was sent.")

        # tweet stuff
        path = f"log_images/{current_time}.jpg"
        # t.tweet_image(status=status, path=path)
        t.send_dm(username="eglootz", path=path, status=f"{alert} @eglootz")

        os.remove(path)
        print("DM with photo was sent.")

    if motion == False:
        current_motion = False
        lc.light("white")
