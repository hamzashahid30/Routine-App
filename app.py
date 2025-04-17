# routine_app.py
import streamlit as st
import time
from datetime import datetime, timedelta

st.title("Aaj Ki Routine")

routine = {
    "12:00": "Uthna aur khud ko taza karna",
    "12:30": "Nashta",
    "13:00": "PUBG Gaming",
    "16:00": "Din ka Khana",
    "16:30": "YouTube Automation ka kaam",
    "17:30": "YouTube Automation ka kaam",
    "18:30": "YouTube Automation ka kaam",
    "19:30": "YouTube Automation ka kaam",
    "20:30": "YouTube Automation ka kaam",
    "21:30": "YouTube Automation ka kaam",
    "22:30": "YouTube Automation ka kaam",
    "23:00": "Raat ka Khana",
    "23:30": "YouTube Automation ka kaam",
    "00:30": "YouTube Automation ka kaam",
    "01:30": "YouTube Automation ka kaam",
    "03:00": "Neend (9 ghante)",
}

def display_routine():
    now = datetime.now()
    current_time_str = now.strftime("%H:%M")
    today = now.date()

    sorted_routine_items = sorted(routine.items())

    for time_str, activity in sorted_routine_items:
        task_hour = int(time_str.split(":")[0])
        task_minute = int(time_str.split(":")[1])
        task_datetime_today = now.replace(hour=task_hour, minute=task_minute, second=0, microsecond=0)

        if task_datetime_today < now:
            # Kaam guzar chuka hai, agar aaj ka hai toh "Ho Gaya" likho, nahi toh "Kal"
            if task_datetime_today.date() == today:
                st.write(f"<span style='color: gray;'>**{time_str}:** {activity} (Ho Gaya)</span>", unsafe_allow_html=True)
            else:
                # Agar time aaj se pehle ka hai toh yeh technically kal ka hi hoga agar routine daily hai
                st.write(f"<span style='color: gray;'>**{time_str}:** {activity} (Kal)</span>", unsafe_allow_html=True)
        elif time_str == current_time_str:
            # Abhi ka time hai
            st.write(f"<span style='color: green; font-weight: bold;'>**{time_str}:** {activity} (Abhi)</span>", unsafe_allow_html=True)
        else:
            # Aane wala time
            st.write(f"**{time_str}:** {activity}")

while True:
    display_routine()
    time.sleep(60) # Har 60 seconds mein refresh karega
