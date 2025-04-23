import streamlit as st 
import random

# App Title
st.title("🌱 Growth Mindset Challenge")

# Intro
st.markdown("""
Welcome to the **Growth Mindset Challenge**!  
Take a new challenge every day and become a better version of yourself 
""")

# Name input
name = st.text_input("Enter your name:")

# List of Daily Challenges
challenges = [
    "Learn something new today – watch a video or read an article.",
    "Appreciate someone today.",
    "Spend 10 minutes in silence – no phone, no distractions.",
    "Write down one goal and take a small step toward it.",
    "Look at a problem from a completely different perspective.",
    "Accept one weakness and plan how to improve it."
]

# Show challenge on button click
if st.button("Get Today's Challenge"):
    if name:
        challenge = random.choice(challenges)
        st.success(f"Hi {name}! Your challenge for today is:\n\n👉 **{challenge}**")
    else:
        st.warning("Please enter your name first! 😊")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
