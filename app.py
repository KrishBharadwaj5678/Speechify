import pyttsx3
import streamlit as st

st.set_page_config(
    page_title="Speechify",
    page_icon="favicon.png",
    menu_items={
        "About":"Transform text into captivating speech effortlessly. Enhance accessibility with clear, natural-sounding narration. Experience seamless text-to-speech conversion for all your content needs."
    }
)

st.write("<h2 style='color:#FF9800';>Text to Clear Speech in Seconds!</h2>",unsafe_allow_html=True)

st.image("text_to_speech.png")

voice_name=st.radio("Select Voice",["Male","Female"],index=0)

voice_rate=st.slider("Set Voice Rate", 1, 500,130)

text=st.text_area("Type your text here")

btn=st.button("Convert To Speech")

def speech(text):
    engine = pyttsx3.init()

    voices=engine.getProperty("voices")
    if(voice_name=="Male"):
        engine.setProperty("voice",voices[0].id)
    elif(voice_name=="Female"):
        engine.setProperty("voice",voices[1].id)

    engine.setProperty('rate', voice_rate)
    engine.say(text)
    engine.runAndWait()

if btn:
    speech(text)