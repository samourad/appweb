import streamlit as st

#Titre
st.title("mon formulaire")

#Texte
st.write("Ceci est un formulaire de contact")

#Champ de saisi
user_input=st.text_input("tapez votre texte : ")

st.write(user_input)
