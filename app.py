import pyttsx3
from groq import Groq
import speech_recognition as sr
import time

client = Groq(
    api_key="YOUR_GROQ_API"
)
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
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
                "role": "system",
                "content": "Replace_with_the_character_and_context_you_want_for_your_assistant!"
            }
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.1-8b-instant",
    )
    return chat_completion.choices[0].message.content

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    recognizer = sr.Recognizer()
    while True:
        print("Say The Wakeword to prompt the model...")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "REPLACE_WITH_YOUR_WAKEWORD":
                    filename = "input.wav"
                    print("You May Speak!")
                    with sr.Microphone() as source:
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, 'wb') as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You: {text}")

                        response = generate_response(text)
                        print(f"Bot: {response}")
                        speak_text(response)

            except Exception as e:
                print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
