print("Gym logger initialized")

import streamlit as st
import random

if "workouts" not in st.session_state:
    st.session_state.workouts = []

messages = [
    "Time to move some heavy circles.",
    "Pain is an illusion, but PRs are real.",
    "Your weakest day now would've been your strongest a year ago.",
    "The only bad workout is the one you didn't do.",
    "Don't stop when you're tired. But probably stop if you get injured.",
    "One day or day one.",
    "Are you a different animal, and the same beast?",
    "7 reps for atrophy.",
    "Someone who works hard can never beat someone who enjoys themselves.",
    "At the end of the day, it's the night.",
    "It's never too late to give up on your dreams.",
    "I lift, therefore I am.",
    "In a war of ego lifting, the loser always wins.",
    "To deload or not to deload, that is the question.",
    "One small rep for a lifter, one giant leap for stimulus.",
    "I'm gonna make you a protein shake you can't refuse.",
    "Do 100 push-ups, 100 sit-ups, 100 squats, and run 10km. But not all together, or you'll go bald.",
    "Let's log... just this once.",
    "One must imagine the sissy squatter happy.",
    "Man is born recovered, and everywhere he is in fatigue.",
    "Life is like a set of dumbbells... You never know what you're gonna get.",
    "The only ones who should lift are those who are prepared to be lifted.",
    "You thought this was a gym logger, but it was me, Dio!",
    "This gym logger is sponsored by RAID: Shadow Legends (jk).",
    "I gently open the door to the gym...",
    "In English, 'hypertrophy', if you split the word it's 'hyper' and 'trophy', so you're hypering trophies.",
    "Every sixty seconds in the gym, a minute passes.",
    "Do you even lift, bro?",
    "You merely adopted the gym. I was born in it.",
    "Call a spotter... but not for me.",
    "But could you do it on a cold, rainy night in Diamond Gym?"
]

st.title("Add a Workout")
st.write(random.choice(messages))

st.header("Workout Details") 

with st.form("workout_form"):
    workout_name = st.text_input("Workout Name")
    workout_date = st.date_input("Workout Date")
    duration = st.number_input(
        "Duration (minutes)",
        min_value=0 
    )
    workout_notes = st.text_area("Workout Notes")
    energy_level = st.slider("Energy level", 0,10)
    workout_submitted = st.form_submit_button("Save Workout")
    if workout_submitted:
        if workout_name:
            workout_id = f"workout_{len(st.session_state.workouts) + 1}"
            new_workout = {
                "id": workout_id,
                "name": workout_name,
                "date": workout_date,
                "duration": duration,
                "notes": workout_notes,
                "energy_level": energy_level,
                "exercises": []
            }
            st.session_state.workouts.append(new_workout)
            st.success("Workout saved!")
            st.rerun()
        else:
            st.error("Please enter a workout name")


