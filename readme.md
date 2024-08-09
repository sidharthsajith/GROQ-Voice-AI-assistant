### Setup:
1) Install the required packages using pip:
`pip install pyttsx3 groq speech_recognition transformers`
2) Replace `YOUR_GROQ_API` with your actual Groq API key.
3) Refer to [Requirements](https://github.com/sidharthsajith/GROQ-Voice-AI-assistant/tree/main#requirements) for the complete setup.
### How to make it work:
Run the script using Python: `python app.py`
Speak the wake word to prompt the model.
Speak your message after the prompt.
The script will utilize the Google Speech Recognition API to transcribe your audio to text.
The script will then employ the Groq AI model, leveraging its Natural Language Processing (NLP) capabilities, to generate a response based on the input text.
The response will be spoken out loud using pyttsx3, utilizing its Text-to-Speech (TTS) functionality.
## Use Cases:
1) Virtual Assistant: This script can be used as a basic virtual assistant that responds to voice commands, utilizing its NLP capabilities to understand and respond to user input.
2) Chatbot: This script can be used as a chatbot that responds to user input, leveraging its ability to generate responses based on input text.
3) Voice-to-Text: This script can be used to transcribe audio to text, utilizing its speech recognition capabilities.
## Theory:
* Speech Recognition: The script employs the speech_recognition library to recognize spoken audio, utilizing its ability to transcribe audio to text.
* Natural Language Processing **(NLP)**: The script utilizes the Groq AI model to generate a response based on the input text, leveraging its NLP capabilities.
* Text-to-Speech: The script employs the pyttsx3 library to convert text to speech, utilizing its TTS functionality.
### Code Explanation:
* The transcribe_audio_to_text function utilizes the speech_recognition library to transcribe audio to text, leveraging its speech recognition capabilities.
* The generate_response function utilizes the Groq AI model to generate a response based on the input text, leveraging its NLP capabilities.
* The speak_text function utilizes the pyttsx3 library to convert text to speech, utilizing its **TTS functionality**.
* The main function is the entry point of the script, utilizing a while loop to continuously listen for audio input and respond accordingly.
## Voice Virtual Assistant
This is a basic virtual assistant that responds to voice commands using the Groq AI model, leveraging its NLP capabilities to understand and respond to user input.

### Usage:

- Run the script using Python: python app.py
- Speak the wake word to setup to prompt the model.
- Speak your message after the prompt.
- The script will transcribe your audio to text using Google Speech Recognition.
- The script will then generate a response using the Groq AI model.
- The response will be spoken out loud using pyttsx3.
### Requirements:
- Python 3.6 or later
- `pip install pyttsx3 groq speech_recognition transformers`
- Replace `YOUR_GROQ_API` with your actual Groq API key.
- Setup the context and the bot character using in the code where I have mentioned `Replace_with_the_character_and_context_you_want_for_your_assistant!` in the code.
- And setup your Bot Wakeword by `replacing REPLACE_WITH_YOUR_WAKEWORD` in the code.
- You may choose the model you like other the mentioned llama-3.1-8b-instant by referring to the available models at [Groq](https://console.groq.com/docs/models) and replace the model by the model id mentioned in the website.
## License:

This script is licensed under the MIT License.
