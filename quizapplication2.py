import streamlit as st

st.title("Paul's Quiz Application")
st.markdown("---------------------------------")

# Initialize session state to keep track of score and progress if needed
if "submitted" not in st.session_state:
  st.session_state.submitted = False

with st.form("quiz_form"):
  # Question 1
  st.markdown("### 1. What is the capital of Nigeria?")
  q1 = st.radio(
      "Select your answer for Q1:",
      ["A. Lagos", "B. Kano", "C. Abuja", "D. Niger"],
      index=None,
      key="q1",
  )

  # Question 2
  st.markdown("### 2. Which language are we using?")
  q2 = st.radio(
      "Select your answer for Q2:",
      ["A. Java", "B. C++", "C. HTML", "D. Python"],
      index=None,
      key="q2",
  )

  # Question 3
  st.markdown("### 3. What does CPU stand for?")
  q3 = st.radio(
      "Select your answer for Q3:",
      [
          "A. Central processing unit",
          "B. Computer personal unit",
          "C. Central people union",
          "D. Computer processing user",
      ],
      index=None,
      key="q3",
  )

  # Question 4
  st.markdown("### 4. Which is not a computer system brand?")
  q4 = st.radio(
      "Select your answer for Q4:",
      ["A. Hp", "B. Bugatti", "C. Dell", "D. Lenovo"],
      index=None,
      key="q4",
  )

  # Question 5
  st.markdown("### 5. What does CIA stand for?")
  q5 = st.radio(
      "Select your answer for Q5:",
      [
          "A. Come induce attack",
          "B. Confidentiality integrity availability",
          "C. Crown intermediate account",
          "D. Corrupt inbox account",
      ],
      index=None,
      key="q5",
  )

  submitted = st.form_submit_button("Submit Quiz")

if submitted:
  score = 0

  # Check answers
  if q1 and q1.startswith("C"):
    score += 1
  if q2 and q2.startswith("D"):
    score += 1
  if q3 and q3.startswith("A"):
    score += 1
  if q4 and q4.startswith("B"):
    score += 1
  if q5 and q5.startswith("B"):
    score += 1

  st.success("Quiz finished!")
  st.metric(label="Your Final Score", value=f"{score} out of 5")

  if score == 5:
    st.balloons()  # Fun celebration animation for a perfect score!
