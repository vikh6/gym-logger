import streamlit as st

st.title("Your Workouts")

if "workouts" not in st.session_state:
    st.session_state.workouts = []


if "disable_set_duration" not in st.session_state:
    st.session_state.disable_set_duration = False

if "disable_rir" not in st.session_state:
    st.session_state.disable_rir = False

if "disable_rpe" not in st.session_state:
    st.session_state.disable_rpe = False

if "disable_tempo" not in st.session_state:
    st.session_state.disable_tempo = False

if "disable_prior_rest_time" not in st.session_state:
    st.session_state.disable_prior_rest_time = False

if "disable_rom" not in st.session_state:
    st.session_state.disable_rom = False

if "disable_form_quality" not in st.session_state:
    st.session_state.disable_form_quality = False

workouts = st.session_state.workouts

if len(workouts) == 0:
    st.write("No workouts yet.")
else:
    for workout in workouts:
        st.header(f"{workout['name']} ({workout['date']})")
        st.write(f" Energy Level: {workout['energy_level']}/10")
        if workout['notes']:
            st.write(f" Notes: {workout['notes']}")
        if workout["exercises"]:
            st.subheader("Exercises:")
            for exercise in workout["exercises"]:
                st.write(f"**{exercise['name']}**")
                if exercise['notes']:
                    st.write(f" Notes: {exercise['notes']}")
                if exercise["sets"]:
                    for s in exercise["sets"]:
                        st.write(f"**Set {len(exercise['sets'])}: {s['reps']} reps at {s['weight']} kg**")
                        st.write(f" - Duration: {s['sduration']} sec, RIR: {s['rir']}, RPE: {s['rpe']}/10")
                        if s['tempo']:
                            st.write(f" - Tempo: {s['tempo']}")
                        if s['rest']:
                            st.write(f" - Prior Rest Time: {s['rest']} sec")
                        if s['rom']:
                            st.write(f" - Range of Motion: {s['rom']}")
                        if s['form'] is not None:
                            st.write(f" - Form Quality: {s['form']}/10")
                        if s['snotes']:
                            st.write(f" - Set Notes: {s['snotes']}")
                else:
                    st.write(" No sets for this exercise.")
                with st.expander(f"Add Set to {exercise['name']}"):
                    weight = st.number_input("Weight (kg)", min_value=0.0, key=f"weight_{exercise['id']}")
                    reps = st.number_input("Reps", min_value=1, key=f"reps_{exercise['id']}")
                    sduration = st.number_input("Duration (sec)", min_value=0, key=f"sduration_{exercise['id']}", disabled=st.session_state.disable_set_duration)
                    rir = st.number_input("RIR (Reps in Reserve)", min_value=0, key=f"rir_{exercise['id']}", disabled=st.session_state.disable_rir)
                    rpe = st.slider("RPE (Rate of Perceived Exertion)", 0,10, key=f"rpe_{exercise['id']}", disabled=st.session_state.disable_rpe)
                    tempo = st.text_input("Tempo (eg, 2-1-2-2)", key=f"tempo_{exercise['id']}", disabled=st.session_state.disable_tempo)
                    rest = st.number_input("Prior Rest Time (sec)", min_value=0, key=f"rest_{exercise['id']}", disabled=st.session_state.disable_prior_rest_time)
                    rom = st.text_input("Range of Motion (eg, Full, Partial)", key=f"rom_{exercise['id']}", disabled=st.session_state.disable_rom)
                    form = st.slider("Form Quality",0,10, key=f"form_{exercise['id']}", disabled=st.session_state.disable_form_quality)
                    snotes = st.text_area("Set Notes", key=f"snotes_{exercise['id']}")
                    with st.expander("Add Additional Reps"):
                        areps_type = st.text_input("Type of Additional Reps (e.g., Drop Set, Rest-Pause)", key=f"areps_type_{exercise['id']}")
                        areps = st.number_input("Additional Reps", min_value=0, key=f"areps_{exercise['id']}")
                        areps_notes = st.text_area("Notes (any changes in weight, ROM, etc.)", key=f"areps_notes_{exercise['id']}")
                    if st.button("Save Additional Reps", key=f"save_areps_{exercise['id']}"):
                        if areps > 0:
                            if "additional_reps" not in exercise:
                                exercise["additional_reps"] = []
                            exercise["additional_reps"].append({
                                "type": areps_type,
                                "reps": areps,
                                "notes": areps_notes
                            })
                            st.success("Additional reps saved!")
                            st.rerun()
                        else:
                            st.error("Please enter a valid number of additional reps.")
                    if st.button("Save Set", key=f"save_set_{exercise['id']}"):
                        exercise["sets"].append({
                            "id": f"set_{len(exercise['sets']) + 1}",
                            "weight": weight,
                            "reps": reps,
                            "sduration": sduration,
                            "rir": rir,
                            "rpe": rpe,
                            "tempo": tempo,
                            "rest": rest,
                            "rom": rom,
                            "form": form,
                            "snotes": snotes
                        })
                        st.rerun()
        else:
            st.write("No exercises yet.")
        with st.expander("Add Exercise"):

            exercise_name = st.text_input("Exercise Name",key=f"name_{workout['id']}")
            exercise_notes = st.text_area("Notes",key=f"notes_{workout['id']}")

            if st.button("Save Exercise",key=f"save_{workout['id']}"):
                workout["exercises"].append({
                    "id": f"exercise_{len(workout['exercises']) + 1}",
                    "name": exercise_name,
                    "notes": exercise_notes,
                    "sets": []
            })
                st.rerun()
        if st.button(f"Delete {workout['name']}", key=workout["id"]):
            st.session_state.workouts = [
                w for w in st.session_state.workouts
        if w["id"] != workout["id"]
            ]
            st.success(f"Deleted {workout['name']}")
            st.rerun()


st.checkbox(
    "Disable  set duration",
    value=st.session_state.disable_set_duration,
    key="disable_set_duration"
)

st.checkbox(
    "Disable  RIR",
    value=st.session_state.disable_rir,
    key="disable_rir"  
)

st.checkbox(
    "Disable  RPE",
    value=st.session_state.disable_rpe,
    key="disable_rpe"  
)

st.checkbox(
    "Disable tempo",
    value=st.session_state.disable_tempo,
    key="disable_tempo"
)

st.checkbox(
    "Disable prior rest time",
    value=st.session_state.disable_prior_rest_time,
    key="disable_prior_rest_time"
)

st.checkbox(
    "Disable ROM",
    value=st.session_state.disable_rom,
    key="disable_rom"  
)

st.checkbox(
    "Disable form quality",
    value=st.session_state.disable_form_quality,
    key="disable_form_quality"
)