import streamlit as st

st.title("Even and Odd Number Sum Calculator")
st.write("This app calculates the sum of even and odd numbers from 1 to 20.")

if st.button("Run Calculation"):
  even_total = 0
  odd_total = 0

  # We use a container to show output cleanly line by line
  output_container = st.container()

  for num in range(1, 21):
    if num % 2 == 0:
      output_container.write(f"{num} is even")
      even_total += num
    output_container.write(f"The sum of even numbers is = {even_total}")

    if num % 2 > 0:
      output_container.write(f"{num} is odd")
      odd_total += num
    output_container.write(f"The sum of odd numbers is = {odd_total}")
    output_container.write("---")  # divider line
