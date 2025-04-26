import streamlit as st
import time

# Title of the app
st.title("Countdown Timer")

# Input for countdown time in seconds
countdown_time = st.number_input("Enter countdown time in seconds:", min_value=1)

# Button to start the countdown
if st.button("Start Countdown"):
    for i in range(countdown_time, 0, -1):
        st.write(f"Time remaining: {i} seconds")
        time.sleep(1)  # Wait for 1 second
    st.write("Time's up!")