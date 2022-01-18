import streamlit as st


st.set_page_config(
    page_title="Encryption by Saaswath",
    page_icon="🔏",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "## Caesar Cipher. \nWith ❤ by *Saaswath*"
    }
)


def encrypt(pt):
    """
    Encrypts the text, based on the caesar cipher scheme with disposition of 12
    :param pt: Plaintext input
    :return ct: Ciphertext output
    """
    ct = ""
    try:
        for i in range(len(pt)):
            char = pt[i]
            if char.isupper():
                ct += chr((ord(char) - 53) % 26 + 65)
            elif char.islower():
                ct += chr((ord(char) - 85) % 26 + 97)
        return ct
    except KeyError:
        st.warning("Character not included in encryption scheme")
        return pt


def decrypt(ct):
    """
    Decrypts the text, based on the caesar cipher scheme with disposition of 12
    :param ct: Ciphertext input
    :return pt: Plaintext output
    """
    pt = ""
    try:
        for i in range(len(ct)):
            char = ct[i]
            if char.isupper():
                pt += chr((ord(char) - 51) % 26 + 65)
            elif char.islower():
                pt += chr((ord(char) - 83) % 26 + 97)
        return pt

    except KeyError:
        st.warning("Character not included in encryption scheme")
        return ct


st.title('Caesar Cipher - With a Shift of 13')
st.markdown('### by Saaswath')
in_txt = st.text_input('Your Message', placeholder="Enter text to encrypt/decrypt")
crypt_opt = st.radio(
    "What do you want to do with the text?",
    ('Encrypt', 'Decrypt'))
if in_txt != "":
    if crypt_opt == "Encrypt":
        st.write("Here is the encipher:")
        st.markdown('**' + encrypt(in_txt) + '**')
    else:
        st.write("Here is the decipher:")
        st.markdown('**' + decrypt(in_txt) + '**')

