# routine_app.py
import streamlit as st
import time
from datetime import datetime, timedelta

st.title("Aaj Ki Routine")

routine = {
    "12:00": {"activity": "Uthna aur khud ko taza karna", "notified": False},
    "12:30": {"activity": "Nashta", "notified": False},
    "13:00": {"activity": "PUBG Gaming", "notified": False},
    "16:00": {"activity": "Din ka Khana", "notified": False},
    "16:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "17:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "18:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "19:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "20:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "21:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "22:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "23:00": {"activity": "Raat ka Khana", "notified": False},
    "23:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "00:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "01:30": {"activity": "YouTube Automation ka kaam", "notified": False},
    "03:00": {"activity": "Neend (9 ghante)", "notified": False},
}

def check_routine():
    now = datetime.now()
    current_time_str = now.strftime("%H:%M")
    current_time_minute = now.minute

    for time_str, task_info in routine.items():
        task_hour = int(time_str.split(":")[0])
        task_minute = int(time_str.split(":")[1])
        task_datetime = now.replace(hour=task_hour, minute=task_minute, second=0, microsecond=0)

        # Check if the task is within the next minute and hasn't been notified yet
        if abs((task_datetime - now).total_seconds()) <= 60 and not task_info["notified"]:
            st.warning(f"**Abhi:** {task_info['activity']}")
            # Optional: Play an alarm sound (browser-dependent and might require user interaction)
            st.components.v1.html("""
                <audio autoplay>
                  <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3" type="audio/mpeg">
                  Your browser does not support the audio element.
                </audio>
            """, height=0)
            routine[time_str]["notified"] = True

def display_routine():
    for time_str, task_info in routine.items():
        st.write(f"**{time_str}:** {task_info['activity']} {'(Notified)' if task_info['notified'] else ''}")

while True:
    check_routine()
    display_routine()
    time.sleep(60) # Check every 60 seconds
