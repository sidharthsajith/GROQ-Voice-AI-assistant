import pyttsx3
from groq import Groq
import speech_recognition as sr
import time

client = Groq(
    api_key="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"
)
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping unknown issue")


def generate_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"You are Arjuna-AI, you are developed by Sidharth Sajith (you may call him as your father), your primary job is to fulfill the tasks given by him just like jarvis does with IronMan, you may keep the Jarvis Tone in your response and do this tasks:{prompt}"
            }
        ],
        model="llama-3.1-8b-instant",
    )
    return (chat_completion.choices[0].message.content)


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main ():
    
