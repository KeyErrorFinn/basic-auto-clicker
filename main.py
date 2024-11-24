import mouse
import keyboard
from datetime import datetime

# Gets the current time right now
start_time = datetime.now()

# The amount of seconds between each click in the loop
time_between_clicks = 120

# Runs a constant loop until broken by the key "L"
while True:
    # Checks the current time with each loop to see if it has been enough time
    current_time = datetime.now()
    if (current_time-start_time).seconds >= 120:
        # Click the left mouse button and resets the start_time
        print(f"Clicked at {current_time}")
        mouse.click('left')
        start_time = current_time
    if keyboard.is_pressed("l"):
        break