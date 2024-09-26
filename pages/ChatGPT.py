import streamlit as st

st.title("ChatGPT-Rédacteur Web")

user_input = st.text_input("Choississez une thématique")

open_key = st.siebar.text_input("Tapez une clé openAI")

#Rédacteur Correction
import os
from openai import OpenAI

client = OpenAI(api_key=OpenAIKEY)



chat_completion = client.chat.completions.create(
    messages=[
         {
          "role": "system",
         "content": f"Tu es un traducteur de langue qui traduit de l'anglais vers le français." +" Si le texte en entrée n'est pas en anglais, tu retournes la phrase : 'Je ne prends que du texte en anglais.'"
         },

        {
            "role": "user",
            "content": "Iphone 13 actualité"
        },

        {
            "role": "assistant",
            "content": "Sujet d'actu : Ils seront en vente à partir du 27 septembre 2021. L'iPhone 13, l'iPhone 13 Pro, l'iPhone 13 Pro Max et l'iPhone 13 Mini gardent le même design que leurs prédécesseurs. Cependant, l'iPhone 13 sera plus épais de 0.25 mm mais cela devrait passer presque inaperçu.",
        },



           {
    "role": "user",
    "content": "Hola todos",
},
{
    "role": "assistant",
    "content": "Je ne prends que du texte en anglais.",
},
    {
    "role": "user",
    "content": "Bonjour tout le monde !",
},
{
    "role": "assistant",
    "content": "Je ne prends que du texte en anglais.",
},




         {
            "role": "user",
            "content": user_input,
        },
    ],
    model="gpt-3.5-turbo",
    temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


# Réponse de ChapGPT
st.write(chat_completion.choices[0].message.content)
