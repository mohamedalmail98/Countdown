import streamlit as st
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="Countdown till you come back",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# Apply custom CSS for space background and text styling
st.markdown("""
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1477201389074-1863f668fac1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .stApp {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 2rem;
        border-radius: 1rem;
    }
    h1 {
        text-align: center;
        color: #00ffff;
        text-shadow: 0 0 20px #00ffff;
    }
    .countdown {
        font-size: 2.5em;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 10px #ffffff;
    }
    </style>
""", unsafe_allow_html=True)






# Title
st.markdown("<h1 style='text-align: center;'>🚀 Countdown till you come back</h1>", unsafe_allow_html=True)
st.markdown("---")

# Target datetime
target_date = datetime(2025, 8, 16, 0, 0, 0)

# Live countdown
placeholder = st.empty()

while True:
    now = datetime.now()
    if now >= target_date:
        placeholder.markdown("<h2 style='text-align: center; color: green;'>🎉 The day has arrived! 🎉</h2>", unsafe_allow_html=True)
        break

    remaining = target_date - now
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    countdown_html = f"""
    <div style="text-align: center; font-size: 2em;">
        <p><strong>{days}</strong> days</p>
        <p><strong>{hours:02}</strong> hours</p>
        <p><strong>{minutes:02}</strong> minutes</p>
        <p><strong>{seconds:02}</strong> seconds</p>
    </div>
    """

    placeholder.markdown(countdown_html, unsafe_allow_html=True)
    time.sleep(1)
