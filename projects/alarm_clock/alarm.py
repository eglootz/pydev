# import the module used to get and set the time
from datetime import datetime

# import the module used to play sounds
from playsound import playsound


alarm_hour = input("Hour (HH): ")

alarm_minute = input("Minute (MM): ")

alarm_seconds = input("Seconds (SS): ")


print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")

    if(alarm_hour == current_hour) and (alarm_minute == current_minute) and (alarm_seconds == current_seconds):
        print("Wake Up!")
        while input().lower != "ok":
            playsound("alarm_sound.mp3")
