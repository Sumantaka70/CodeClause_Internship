import datetime
import tkinter as tk
from tkinter import messagebox
import playsound

def set_alarm():
    alarm_time = entry.get()

    try:
        alarm_hour = int(alarm_time[:2])
        alarm_minute = int(alarm_time[3:5])

        current_time = datetime.datetime.now()
        alarm_datetime = current_time.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)

        if current_time > alarm_datetime:
            # If the alarm time is in the past, add one day to the alarm datetime
            alarm_datetime += datetime.timedelta(days=1)

        time_difference = alarm_datetime - current_time
        total_seconds = time_difference.total_seconds()

        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

        # Wait until the alarm time is reached
        import time
        time.sleep(total_seconds)

        # Play alarm sound
        playsound.playsound('alarma.mp3')

        messagebox.showinfo("Alarm", "Wake up!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid time (HH:MM)")

# Create GUI window
window = tk.Tk()
window.title("Alarm Clock")
window.geometry("300x150")

# Create label and entry for alarm time
label = tk.Label(window, text="Enter alarm time (HH:MM):")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create set alarm button
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Run the GUI event loop
window.mainloop()
