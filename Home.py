import streamlit as st

#Titre
st.title("mon formulaire")

#Texte
st.write("Ceci est un formulaire de contact")

#Champ de saisi
user_input=st.text_input("tapez votre texte : ")

st.write(user_input)

#Image
st.image("https://www.google.com/imgres?q=eemi&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D100063733442303&imgrefurl=https%3A%2F%2Fwww.facebook.com%2Feemi75%2F&docid=liTig4DeeUiMMM&tbnid=Je8AhCyNeMtwLM&vet=12ahUKEwi786zUzOCIAxWJT6QEHQeAL_YQM3oECE0QAA..i&w=360&h=360&hcb=2&ved=2ahUKEwi786zUzOCIAxWJT6QEHQeAL_YQM3oECE0QAA")
