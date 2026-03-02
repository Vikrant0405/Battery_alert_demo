import psutil
import time
from plyer import notification
import  pyttsx3
speak = pyttsx3.init()

# Track previous charger state to detect changes
prev_power_plugged = None

while True:
    battery = psutil.sensors_battery()
    
    # High battery alert (>= 80% and charging)
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

        time.sleep(60)  # check every 1 minute
    
    # Low battery alert (< 20%) - alerts when charger was connected but now unplugged
    elif battery.percent < 20:
        
        # Check if charger was just unplugged (state changed from True to False)
        if prev_power_plugged == True and battery.power_plugged == False:
            # Charger was unplugged - stop the message, no alert needed now
            print("Charger unplugged - stopping alert")
            prev_power_plugged = battery.power_plugged
            time.sleep(1)  # check every 1 second
        elif battery.power_plugged:
            # Charger is connected but battery is low
            notification.notify(
                title="🔋 Low Battery",
                message=f"Battery is at {battery.percent}%. Please plug in the charger!",
                timeout=5
            )
            voices = speak.getProperty('voices')
            speak.setProperty('voice', voices[1].id)
            speak.setProperty('volume', 1.0)
            speak.setProperty('rate', 160)
            speak.say(f"Battery is low at {battery.percent} percent. Please plug in the charger, it is connected!")
            speak.runAndWait()
            
            prev_power_plugged = battery.power_plugged
            time.sleep(60)  # check every 1 minute
        else:
            # Charger is not connected and battery is low
            notification.notify(
                title="🔋 Low Battery",
                message=f"Battery is at {battery.percent}%. Please connect the charger!",
                timeout=5
            )
            voices = speak.getProperty('voices')
            speak.setProperty('voice', voices[1].id)
            speak.setProperty('volume', 1.0)
            speak.setProperty('rate', 160)
            speak.say(f"Battery is low at {battery.percent} percent. Please connect the charger!")
            speak.runAndWait()
            
            prev_power_plugged = battery.power_plugged
            time.sleep(60)  # check every 1 minute
    else:
        # Update previous state when battery is normal
        prev_power_plugged = battery.power_plugged
        time.sleep(1)  # check every 1 second



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
