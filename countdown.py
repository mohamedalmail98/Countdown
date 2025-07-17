import streamlit as st
from datetime import datetime
import time
import random

# --- Page Configuration ---
st.set_page_config(
    page_title="Countdown till you come back",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS: Space Background & Fully White Fonts ---
st.markdown("""
    <style>
    html, body, [class*="css"], .stMarkdown, .stText, .stTitle, .stHeader,
    .stSubheader, .stCaption, .stLabel, .stDataFrame, .stProgress {
        color: white !important;
    }
    body::before {
        content: "";
        position: fixed;
        top: 0; left: 0;
        height: 100vh; width: 100vw;
        background-image: url('https://img.freepik.com/premium-photo/blue-copy-space-digital-abstract-background_731790-155500.jpg?semt=ais_hybrid&w=740');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        z-index: -1;
        opacity: 6;
        filter: brightness(1.3);
    }
    #overlay-image {
    position: fixed;
    top: 50%;   /* vertical center */
    left: 50%;  /* horizontal center */
    transform: translate(-50%, -50%);
    z-index: 0;  /* above background but below UI (which usually has z-index > 0) */
    opacity: 0.3; /* optional transparency */
    max-width: 400px; /* scale it */
    pointer-events: none; /* so it doesn’t block clicks */
}
    st.markdown("""
    <style>
    /* Your CSS here */
    </style>
    <img id="overlay-image" src="https://pngimg.com/uploads/astronaut/astronaut_PNG33.png" />
""", unsafe_allow_html=True)



        

    .stApp {
        background-color: rgba(0, 0, 0, 0.75);
        padding: 2rem;
        border-radius: 1rem;
    }
    .fact {
        text-align: center;
        font-style: italic;
        margin-top: 20px;
        font-size: 1.1em;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

fact_categories = {
    "21_30": [
        "The Moon completes an orbit of Earth in about 27.3 days — just like your countdown window.",
        "In 30 days, the ISS completes about 480 orbits around Earth.",
        "The Mars Perseverance rover landed after a 7-month journey — your wait is much shorter!",
        "A lunar month lasts ~29.5 days — your countdown is aligned with one full moon cycle."
    ],
    "14_21": [
        "The Sun rotates once every ~24 days at its equator — you're syncing with a solar spin.",
        "Astronauts aboard the ISS see 16 sunrises and sunsets **every day** — over 300 in 20 days!",
        "Solar storms can take 2–3 days to reach Earth — space weather is always on the move."
    ],
    "7_14": [
        "Time moves slightly slower on the ISS than on Earth — relativity at work in just days.",
        "The first human spent only 108 minutes in space — your countdown is far longer!",
        "In 10 days, a satellite in low Earth orbit can circle Earth 160 times."
    ],
    "3_7": [
        "Astronauts begin final suit fittings and quarantine around 5–7 days before launch.",
        "A space shuttle mission typically lasted 5–7 days — you're in that final mission window.",
        "During final prep, astronauts rehearse critical procedures daily for a week straight."
    ],
    "1_3": [
        "A typical ISS spacewalk lasts around 6.5 hours — imagine floating above Earth for that long.",
        "Final checkouts for a space mission are often done 48 hours before launch.",
        "SpaceX missions often complete docking within 1–2 days of launch."
    ],
    "final_day": [
        "At the speed of light, you could reach the Moon in just 1.3 seconds.",
        "Relativity says that even 1 day in space passes differently depending on velocity and gravity.",
        "The Apollo 11 crew spent their final Earth night in a special quarantine facility."
    ],
    "complete": [
        "🎉 Mission complete! Like a returning astronaut, you're back in Earth's time zone.",
        "🌍 The countdown ends — and your journey begins again. Welcome back.",
        "🪐 Time’s up — the stars waited, and so did we."
    ]
}

def get_facts_list_for_remaining_time(remaining_days):
    if 21 <= remaining_days <= 30:
        return fact_categories["21_30"]
    elif 14 <= remaining_days < 21:
        return fact_categories["14_21"]
    elif 7 <= remaining_days < 14:
        return fact_categories["7_14"]
    elif 3 <= remaining_days < 7:
        return fact_categories["3_7"]
    elif 1 <= remaining_days < 3:
        return fact_categories["1_3"]
    elif 0 <= remaining_days < 1:
        return fact_categories["final_day"]
    else:
        return fact_categories["complete"]

# Countdown dates
start_date = datetime(2025, 7, 16, 0, 0, 0)
target_date = datetime(2025, 8, 16, 0, 0, 0)

st.markdown("<h1 style='text-align: center;'>🚀 Countdown till you come back</h1>", unsafe_allow_html=True)
st.markdown("---")

# Placeholder for updating UI
placeholder = st.empty()

# Initialize session state variables for fact cycling
if 'fact_index' not in st.session_state:
    st.session_state.fact_index = 0
if 'last_fact_time' not in st.session_state:
    st.session_state.last_fact_time = time.time()

while True:
    now = datetime.now()
    total_duration = (target_date - start_date).total_seconds()
    elapsed = max(0, (now - start_date).total_seconds())
    remaining = target_date - now
    percent_complete = max(0, min(100, (elapsed / total_duration) * 100))

    if now >= target_date:
        with placeholder.container():
            st.markdown("<h2 style='text-align: center; color: lightgreen;'>🎉 The day has arrived! 🎉</h2>", unsafe_allow_html=True)
            st.progress(1.0)
            st.markdown("**100% completed**")
            # Show a final fact
            facts_list = fact_categories["complete"]
            fact_to_show = facts_list[st.session_state.fact_index % len(facts_list)]
            st.markdown(f"<div class='fact'>🌌 {fact_to_show}</div>", unsafe_allow_html=True)
        break  # countdown finished, exit loop

    else:
        days = remaining.days
        hours, rem = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        # Update fact every 6 seconds
        facts_list = get_facts_list_for_remaining_time(days)
        current_time = time.time()
        if current_time - st.session_state.last_fact_time > 7:
            st.session_state.fact_index = (st.session_state.fact_index + 1) % len(facts_list)
            st.session_state.last_fact_time = current_time
        fact_to_show = facts_list[st.session_state.fact_index]

        countdown_html = f"""
        <div style="text-align: center; font-size: 2em;">
            <p><strong>{days}</strong> days</p>
            <p><strong>{hours:02}</strong> hours</p>
            <p><strong>{minutes:02}</strong> minutes</p>
            <p><strong>{seconds:02}</strong> seconds</p>
        </div>
        """
        with placeholder.container():
            st.markdown(countdown_html, unsafe_allow_html=True)
            st.progress(percent_complete / 100)
            st.markdown(f"**{percent_complete:.2f}% completed**")
            st.markdown(f"<div class='fact'>🌌 {fact_to_show}</div>", unsafe_allow_html=True)

    time.sleep(1)


