import streamlit as st

st.title("🏝️ Treasure Island Adventure")
st.write("THINK BEYOND THE BOX! The questions ahead may be trickier than they look.")

# Initialize game state so the game doesn't reset on every click
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.message = ""

# Step 1: Crossroad
if st.session_state.step == 1:
    st.subheader("You are at a crossroad. Where do you want to go?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go Left"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("Go Right"):
            st.session_state.game_over = "You fell into a hole. Game over."
            st.session_state.step = "over"
            st.rerun()

# Step 2: River
elif st.session_state.step == 2:
    st.subheader("You have reached a river. What do you want to do?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Swim"):
            st.session_state.game_over = "You were attacked by trout. Game over."
            st.session_state.step = "over"
            st.rerun()
    with col2:
        if st.button("Wait"):
            st.session_state.step = 3
            st.rerun()

# Step 3: Doors
elif st.session_state.step == 3:
    st.subheader("You are before three doors. Which door do you choose?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Red Door"):
            st.session_state.game_over = "You were burned by fire. Game over."
            st.session_state.step = "over"
            st.rerun()
    with col2:
        if st.button("Yellow Door"):
            st.session_state.game_over = "You were eaten by beasts. Game over."
            st.session_state.step = "over"
            st.rerun()
    with col3:
        if st.button("Blue Door"):
            st.session_state.game_over = "You Win! You found the treasure! 🎉"
            st.session_state.step = "over"
            st.rerun()
