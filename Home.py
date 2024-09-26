import streamlit as st

#Titre
st.title("mon formulaire")

#Texte
st.write("Ceci est un formulaire de contact")

#Champ de saisi
user_input=st.text_input("tapez votre texte : ")

st.write(user_input)

#Image
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbMZFucLMvnC70v26VRtwnsv73EX8FpKxCqA&s")

#Sidebare
st.sidebar.title("Ali Mouradi")

#Vidéo dans la sidebar
st.sidebar.video("https://youtu.be/VUkm6b58bMo")

#select Bare
student_grad = st.selectbox("Selectionnez votre niveau d'étude", ["Bac", "Bac+2", "Bac+5"])

#Select slider
age = st.select_slider("Quel est votre âge ?", range(0,99))

#Condition en python
if age > 18:
  st.write("Vous êtes majeur")
else:
  st.write("Vous êtes mineur")
