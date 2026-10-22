from plyer import notification
import pyttsx3
import time
from datetime import datetime

engine = pyttsx3.init()

medicine_name = "Paracetamol"
medicine_time = "11:55"   # Change this time

while True:

    current_time = datetime.now().strftime("%H:%M")

    print("Current Time:", current_time)

    if current_time == medicine_time:

        notification.notify(
            title="Medicine Reminder",
            message=f"Time to take {medicine_name}",
            timeout=10
        )

        engine.say(f"Time to take {medicine_name}")
        engine.runAndWait()

        time.sleep(60)

    time.sleep(1)