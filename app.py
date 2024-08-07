import pyttsx3
from groq import Groq
import speech_recognition as sr
import time

client = Groq(
    api_key="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"
)
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google()
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
        model="mixtral-8x7b-32768",
    )
    return (chat_completion.choices[0].message.content)




def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        print("Say Arjuna to prompt the model...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "arjuna":
                    filename: "input.wav"
                    print("You May Speak!")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, 'wb') as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)
                    if text:
                        print (f"You: {text}")

                        response = generate_response(text)
                        print = (f"ArjunaAI: {response}")
                        speak_text(response)

            except Exception as e:
                print("An error occured: {}".format(e))

if __name__ == "__main__":
    main()