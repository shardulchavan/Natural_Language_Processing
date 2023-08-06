Speech-Enabled Notepad and Text Summarization Projects

This repository contains two projects: Speech Enabled Notepad and Text Summarization.

Speech Enabled Notepad
The Speech Enabled Notepad is a software application developed using Python's NLTK (Natural Language Toolkit) and Speech Recognition libraries. It allows users to convert multilingual speech-to-text and text-to-speech in six different languages. With the help of the Speech Recognition API, the software transcribes spoken words into written text, making it easy to take notes or create written documents using speech input. Additionally, it uses Google Text to Speech (gtts) API to convert written text back to speech, enabling users to listen to their transcribed notes.

Text Summarization
The Text Summarization project is an NLP (Natural Language Processing) application that performs text summarization on the transcribed speech from the Speech Enabled Notepad. It uses feature representation techniques, including word embeddings using the GloVe (Global Vectors for Word Representation) model, to represent the transcribed text efficiently. The project also employs the page rank algorithm to order phrases based on weights assigned during the feature representation process. This enables the system to generate concise and informative summaries of the transcribed text.

Key Features
Speech-to-Text: Convert speech in multiple languages to written text using the Speech Recognition API.
Text-to-Speech: Convert written text back to speech in multiple languages using the Google Text-to-Speech (gtts) API.
Text Summarization: Create extractive summaries of the transcribed text using feature representation and the page rank algorithm.
How to Use
Install the required Python libraries using pip install -r requirements.txt.
Run the Speech Enabled Notepad application to record and transcribe your speech.
Use the Text Summarization application to generate summaries of the transcribed text.
Explore and experiment with different languages and texts to see the capabilities of the projects.
Feel free to contribute, provide feedback, and suggest improvements to enhance the functionality and performance of these projects. Happy coding!
