import time
from tkinter import *
from tkinter import ttk
import winsound

def converter(hours, minutes, seconds):
    """Converts hours, minutes, and seconds into total seconds."""
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

def start_countdown():
    """Starts the countdown based on the input values."""
    total_seconds = converter(hour_entry.get(), minute_entry.get(), second_entry.get())
    input_window.destroy()  # Close the input window
    countdown(total_seconds)

def countdown(total_seconds):
    """Performs the countdown and shows the 'DONE' message."""
    seconds_left = total_seconds
    
    while seconds_left != 0:
        time.sleep(1)
        seconds_left -= 1

    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    # Display the 'DONE' message in a new window
    root = Tk()
    root.geometry("1500x1500")
    frm = ttk.Frame(root, width=1500, height=1500, padding=10)
    frm.grid()
    ttk.Label(frm, text="DONE").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    # Bring the 'DONE' window to the front
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)
    root.lift()
    root.focus_force()
    root.mainloop()

# Create the initial input window
input_window = Tk()
input_window.title("Input Time")

# Create and place the entry fields for hours, minutes, and seconds
ttk.Label(input_window, text="HH").grid(column=0, row=0)
hour_entry = ttk.Entry(input_window, width=5)
hour_entry.grid(column=1, row=0)

ttk.Label(input_window, text="MM").grid(column=2, row=0)
minute_entry = ttk.Entry(input_window, width=5)
minute_entry.grid(column=3, row=0)

ttk.Label(input_window, text="SS").grid(column=4, row=0)
second_entry = ttk.Entry(input_window, width=5)
second_entry.grid(column=5, row=0)

# Create and place the start button
start_button = ttk.Button(input_window, text="Start", command=start_countdown)
start_button.grid(column=2, row=1, columnspan=2)

input_window.mainloop()
