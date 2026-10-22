import random
import string
import streamlit as st

# App Title and Description
st.title("🔐 Secure Password Generator")
st.write("Generate a secure password and share it with your friends!")

# Use a slider for password length instead of input()
length = st.slider("Select password length:", min_value=4, max_value=32)

# Button to trigger password generation
if st.button("Generate Password"):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*"
    
    
    password = ""

    # Guarantee at least one of each character type
    password += random.choice(uppercase)
    password += random.choice(lowercase)
    password += random.choice(numbers)
    password += random.choice(symbols)
     
    characters = uppercase + lowercase + numbers + symbols

    # Fill the rest of the password length
    for i in range(length - 4):
        password += random.choice(characters)

    # Display the result in the app
    st.success("Generated Password:")
    st.code(password, language="")
