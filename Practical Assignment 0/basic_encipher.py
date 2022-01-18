import streamlit as st

def encrypt():
st.title('Substitution Cipher')
in_text = st.text_input('Text', 'Life of Brian', placeholder="Enter text to encrypt/decrypt")
crypt_opt = st.radio(
    "What do you want to do with the text?",
    ('Encrypt', 'Decrypt'))

if crypt_opt == "Encrypt":
    st.write("Here is the encipher.")
else:
    st.write("Here is the decipher.")
