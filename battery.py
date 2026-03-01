import psutil
import time
from plyer import notification
import  pyttsx3
speak = pyttsx3.init()

while True:
    battery = psutil.sensors_battery()
    if battery.percent >= 80 and battery.power_plugged:

        notification.notify(
            title="🔋 Battery Full",
            message="Battery is fully charged. Please unplug the charger!",
            timeout=5
        )
        voices = speak.getProperty('voices')
        # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        speak.setProperty('voice', voices[1].id)

        volume = speak.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        # print(volume)  # printing current volume level
        speak.setProperty('volume', 1.0)

        rate = speak.getProperty('rate')  # getting details of current speaking rate
        # print(rate)  # printing current voice rate
        speak.setProperty('rate', 160)
        speak.say("Battery is fully charged. Please unplug the charger!")
        speak.runAndWait()

        time.sleep(1)  # check every 1 minute
    else:
        time.sleep(1)  # check every 1 minute



#
# import psutil
# import time
# from plyer import notification
#
# while True:
#     battery = psutil.sensors_battery()
#     percent = battery.percent
#     plugged = battery.power_plugged
#
#     # Notify when battery is at or above 95% and still charging
#     if percent >= 95 and plugged:
#         notification.notify(
#             title="🔋 Battery Full",
#             message=f"Battery is at {percent}%. Please unplug the charger!",
#             timeout=10
#         )
#         time.sleep(300)  # wait 5 minutes before next reminder
#     else:
#         time.sleep(60)  # check every 1 minute
