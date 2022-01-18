import streamlit as st
import string

enc_map = {}
dec_map = {}
k = 5
alphabet = string.ascii_letters


# Encryption mapping
for i in range(len(alphabet)):
    enc_map[alphabet[i]] = alphabet[(i + k) % len(alphabet)]
enc_map.update({' ': ' '})


# Decryption mapping
def inv_map():
    for enc, dec in enc_map.items():
        dec_map[dec] = enc


def encrypt(pt):
    """
    Encrypts the text based on the substitution encryption map
    :param pt: Plaintext input
    :return ct: Ciphertext output
    """

    ct = ''
    try:
        for p in pt:
            tmp = enc_map[p]
            ct += tmp
        return ct
    except KeyError:
        st.warning("Character not included in encryption scheme")
        return pt


def decrypt(ct):
    """
    Decrypts the text, based on the substitution decryption map
    :param ct: Ciphertext input
    :return pt: Plaintext output
    """
    inv_map()
    pt = ""
    try:
        for c in ct:
            tmp = dec_map[c]
            pt += tmp
        return pt
    except KeyError:
        st.warning("Character not included in encryption scheme")
        return ct


st.title('Substitution Cipher Tryout')
in_txt = st.text_input('Text', placeholder="Enter text to encrypt/decrypt")
crypt_opt = st.radio(
    "What do you want to do with the text?",
    ('Encrypt', 'Decrypt'))

if crypt_opt == "Encrypt":
    st.write("Here is the encipher:")
    st.markdown('**' + encrypt(in_txt) + '**')
else:
    st.write("Here is the decipher:")
    st.markdown('**' + decrypt(in_txt) + '**')
