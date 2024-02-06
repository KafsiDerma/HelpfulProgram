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
    initialize_countdown_window(total_seconds)

def initialize_countdown_window(total_seconds):
    """Initializes and positions the countdown window."""
    countdown_window = Tk()
    countdown_window.title("Countdown Timer")

    # Position the window at the bottom right corner of the screen
    window_width = 150
    window_height = 100
    screen_width = countdown_window.winfo_screenwidth()
    screen_height = countdown_window.winfo_screenheight()
    x_coordinate = screen_width - window_width - 10  # 10 pixels from the screen's right edge
    y_coordinate = screen_height - window_height - 50  # 50 pixels from the screen's bottom edge

    countdown_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Configure the countdown label
    countdown_label = ttk.Label(countdown_window, text="00:00:00", font=("Helvetica", 16))
    countdown_label.pack(expand=True)

    update_countdown(countdown_window, countdown_label, total_seconds)

    countdown_window.mainloop()

def update_countdown(countdown_window, countdown_label, seconds_left):
    """Updates the countdown every second."""
    if seconds_left > 0:
        # Format seconds into HH:MM:SS
        hours, remainder = divmod(seconds_left, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        countdown_window.after(1000, update_countdown, countdown_window, countdown_label, seconds_left-1)
    else:
        for x in range(0,10,1):
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        countdown_label.config(text="DONE!")

# Create the initial input window
input_window = Tk()
input_window.title("Input Time")

# Center the input window on the screen
window_width = 300
window_height = 100
screen_width = input_window.winfo_screenwidth()
screen_height = input_window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
input_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Create and place the entry fields for hours, minutes, and seconds
ttk.Label(input_window, text="HH").pack(side=LEFT)
hour_entry = ttk.Entry(input_window, width=3)
hour_entry.pack(side=LEFT)
hour_entry.insert(0, "00")  # Default value for hours
ttk.Label(input_window, text="MM").pack(side=LEFT)
minute_entry = ttk.Entry(input_window, width=3)
minute_entry.pack(side=LEFT)
minute_entry.insert(0, "00")  # Default value for minutes
ttk.Label(input_window, text="SS").pack(side=LEFT)
second_entry = ttk.Entry(input_window, width=3)
second_entry.pack(side=LEFT)
second_entry.insert(0, "00")  # Default value for seconds, for example, 30 seconds

# Create and place the start button
start_button = ttk.Button(input_window, text="Start", command=start_countdown)
start_button.pack(side=RIGHT)

input_window.mainloop()
