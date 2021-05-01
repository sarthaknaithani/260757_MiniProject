import datetime
import os
import time
import random
import webbrowser

if not os.path.isfile("alarm_links.txt"):
    print('Creating "alarm_links.txt"...')
    with open("alarm_links.txt", "w") as link_file:
        link_file.write("https://www.youtube.com/watch?v=_XYNLTJe2-0")
        
        
def user_input_check(alarm_sec):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_sec) == 1:
        if alarm_sec[0] < 24 and alarm_sec[0] >= 0:
            return True
    if len(alarm_sec) == 2:
        if alarm_sec[0] < 24 and alarm_sec[0] >= 0 and alarm_sec[1] < 60 and alarm_sec[1] >= 0:
            return True
    elif len(alarm_sec) == 3:
        if alarm_sec[0] < 24 and alarm_sec[0] >= 0 and alarm_sec[1] < 60 and alarm_sec[1] >= 0 and alarm_sec[2] < 60 and alarm_sec[2] >= 0:
            return True
    return False


print("Enter a time for the alarm that should be greater than current time (Ex. 12:30 or 19:45:50)")

while True:
    setalarm = input(">>>> ")
    try:
        alarm_sec = [int(n) for n in setalarm.split(":")]
        if user_input_check(alarm_sec):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Enter time in HH:MM or HH:MM:SS format")

seconds_hms = [3600, 60, 1]
alarm_seconds = sum([x*y for x,y in zip(seconds_hms[:len(alarm_sec)], alarm_sec)])

now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

time_diff_seconds = alarm_seconds - current_time_seconds

if time_diff_seconds < 0:
    print("Enter time greater than->>", datetime.datetime.now().strftime("%H:%M:%S"))
else:

    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

    time.sleep(time_diff_seconds)

    print("...........REMINDER TO WATCH VIDEO IN YOUTUBE....... ")

    with open("alarm_links.txt", "r") as link_file:
        videos = link_file.readlines()

    webbrowser.open(random.choice(videos))
