import streamlit as st
from datetime import datetime, timedelta
import time

# --- Page Config ---
st.set_page_config(page_title="Countdown to Launch", layout="centered")

# --- CSS for Background and Style ---
page_bg = """
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: white;
    font-family: 'Orbitron', sans-serif;
}

h1, h2, h3 {
    color: #ffffff;
    text-align: center;
}

.countdown {
    font-size: 3em;
    font-weight: bold;
    text-align: center;
    color: #00ffff;
    margin-top: 30px;
}

.footer {
    font-size: 0.8em;
    text-align: center;
    color: #ccc;
    margin-top: 50px;
}
</style>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
"""

st.markdown(page_bg, unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>🚀 Countdown to August 16, 2025</h1>", unsafe_allow_html=True)

# --- Target Date ---
target_date = datetime(2025, 8, 16, 0, 0, 0)

# --- Calculate Time Remaining ---
now = datetime.now()
if now >= target_date:
    st.markdown("<div class='countdown'>🎉 The countdown has ended!</div>", unsafe_allow_html=True)
else:
    time_left = target_date - now
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_str = f"{days} days, {hours:02} hours, {minutes:02} minutes, {seconds:02} seconds"
    st.markdown(f"<div class='countdown'>{countdown_str}</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>Made with ❤️ using Streamlit • Sharjah Space Enthusiast</div>", unsafe_allow_html=True)
