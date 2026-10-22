from tkinter import *
from tkinter import messagebox
from plyer import notification
import pyttsx3
import time
from datetime import datetime
import threading

root = Tk()
root.title("AI Medicine Reminder")
root.geometry("400x300")

engine = pyttsx3.init()

Label(root, text="Medicine Name").pack(pady=10)
medicine_entry = Entry(root, width=30)
medicine_entry.pack()

Label(root, text="Medicine Time (HH:MM)").pack(pady=10)
time_entry = Entry(root, width=30)
time_entry.pack()

def start_reminder():

    medicine = medicine_entry.get()
    reminder_time = time_entry.get()

    messagebox.showinfo(
        "Reminder Saved",
        f"{medicine} reminder set at {reminder_time}"
    )

    def check_time():

        while True:

            current_time = datetime.now().strftime("%H:%M")

            print(current_time)

            if current_time == reminder_time:

                notification.notify(
                    title="Medicine Reminder",
                    message=f"Time to take {medicine}",
                    timeout=10
                )

                engine.say(f"Time to take {medicine}")
                engine.runAndWait()

                break

            time.sleep(1)

    threading.Thread(target=check_time).start()

Button(root, text="Save Reminder", command=start_reminder).pack(pady=20)

root.mainloop()