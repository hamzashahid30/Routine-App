# routine_app.py
import streamlit as st

st.title("Aaj Ki Routine")

routine = {
    "12:00 PM - 12:30 PM": "Uthna aur khud ko taza karna",
    "12:30 PM - 1:00 PM": "Nashta",
    "1:00 PM - 4:00 PM": "PUBG Gaming",
    "4:00 PM - 4:30 PM": "Din ka Khana",
    "4:30 PM - 5:30 PM": "YouTube Automation ka kaam",
    "5:30 PM - 6:30 PM": "YouTube Automation ka kaam",
    "6:30 PM - 7:30 PM": "YouTube Automation ka kaam",
    "7:30 PM - 8:30 PM": "YouTube Automation ka kaam",
    "8:30 PM - 9:30 PM": "YouTube Automation ka kaam",
    "9:30 PM - 10:30 PM": "YouTube Automation ka kaam",
    "10:30 PM - 11:00 PM": "YouTube Automation ka kaam",
    "11:00 PM - 11:30 PM": "Raat ka Khana",
    "11:30 PM - 12:30 AM": "YouTube Automation ka kaam",
    "12:30 AM - 1:30 AM": "YouTube Automation ka kaam",
    "1:30 AM - 3:00 AM": "YouTube Automation ka kaam",
    "3:00 AM - 12:00 PM": "Neend (9 ghante)"
}

for time, activity in routine.items():
    st.write(f"**{time}:** {activity}")

st.subheader("Breaks:")
st.write("Har ghante ke baad 5-7 minute ka break lein.")
