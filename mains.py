from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("AI Medicine Reminder")
root.geometry("400x300")

Label(root, text="Medicine Name").pack(pady=10)

medicine_entry = Entry(root, width=30)
medicine_entry.pack()

Label(root, text="Medicine Time (HH:MM)").pack(pady=10)

time_entry = Entry(root, width=30)
time_entry.pack()

def save_medicine():

    medicine = medicine_entry.get()
    med_time = time_entry.get()

    messagebox.showinfo(
        "Saved",
        f"Medicine: {medicine}\nTime: {med_time}"
    )

Button(root, text="Save Reminder", command=save_medicine).pack(pady=20)

root.mainloop()