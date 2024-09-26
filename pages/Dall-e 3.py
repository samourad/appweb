mageimport streamlit as st
st.title("Dall-E 3")

#Champ de saisi
user_input=st.text_input("tapez votre texte : ")

# Champ de saisie dans la slidebar(pour la clé OpenIA)
open_key=st.sidebar.text_input ("Renseignez la clé openAI")

#interaction avec OpenAI
from openai import OpenAI

client = OpenAI(api_key=OpenAI_KEY)
image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)
st.write(user_input)

#Sidebare
st.sidebar.text_input("Clé OpenAI")

#Sidebare
st.sidebar.title("intéraction avec openAI")

#Image
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXuDvlNDmDGF5QwPETEs3eh7RHNGmKBpgwyw&s")


