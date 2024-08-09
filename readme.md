## **Setup:**

1. Install the required packages using pip:

```
pip install pyttsx3 groq speech_recognition
```

2. Replace `YOUR_GROQ_API` with your actual Groq API key.
3. And refer to [Requirements](###Requirements:) for the complete setup.

## **How to make it work:**

1. Run the script using Python: `python main.py`
2. Speak the wake word "arjuna" to prompt the model.
3. Speak your message after the prompt.
4. The script will transcribe your audio to text using Google Speech Recognition.
5. The script will then generate a response using the Groq AI model.
6. The response will be spoken out loud using pyttsx3.

## **Use Cases:**

1. Virtual Assistant: This script can be used as a basic virtual assistant that responds to voice commands.
2. Chatbot: This script can be used as a chatbot that responds to user input.
3. Voice-to-Text: This script can be used to transcribe audio to text.

## **Theory:**

1. Speech Recognition: The script uses the speech_recognition library to recognize spoken audio.
2. Natural Language Processing (NLP): The script uses the Groq AI model to generate a response based on the input text.
3. Text-to-Speech: The script uses the pyttsx3 library to convert text to speech.

## **Code Explanation:**

1. The `transcribe_audio_to_text` function uses the speech_recognition library to transcribe audio to text.
2. The `generate_response` function uses the Groq AI model to generate a response based on the input text.
3. The `speak_text` function uses the pyttsx3 library to convert text to speech.
4. The `main` function is the entry point of the script. It uses a while loop to continuously listen for audio input and respond accordingly.

# ArjunaAI Virtual Assistant

This is a basic virtual assistant that responds to voice commands using the Groq AI model.

**Usage:**

1. Run the script using Python: `python main.py`
2. Speak the wake word to setup to prompt the model.
3. Speak your message after the prompt.
4. The script will transcribe your audio to text using Google Speech Recognition.
5. The script will then generate a response using the Groq AI model.
6. The response will be spoken out loud using pyttsx3.

### **Requirements:**

- Python 3.6 or later
- pip install pyttsx3 groq speech_recognition
- Replace `YOUR_GROQ_API` with your actual Groq API key.
- Setup the context and the bot character using in the code where I have mentioned `Replace_with_the_character_and_context_you_want_for_your_assistant!`
- And setup your Bot Wakeword by replacing `REPLACE_WITH_YOUR_WAKEWORD`
- You may choose the model you like other the mentioned `llama-3.1-8b-instant` by referring to the available models at [Groq](https://console.groq.com/docs/models) and replace the model by the model id mentioned in the website.

**License:**

This script is licensed under the MIT License.
