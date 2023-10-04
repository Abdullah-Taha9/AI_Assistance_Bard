# Code Documentation

## 1. Importing Libraries

```python
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from bardapi import Bard
import requests
```
speech_recognition: Library for speech recognition.
pyttsx3: Library for text-to-speech conversion.
os: Library for interacting with the operating system.
dotenv: Library for loading environment variables from a file.
bardapi: A module that allows interaction with the Bard API.
requests: Library for making HTTP requests.


## 2. Loading Environment Variables
```python
load_dotenv()
BARD_KEY = os.getenv('BARDKEY')
os.environ["_BARD_API_KEY"] = BARD_KEY
```
load_dotenv: Loads environment variables from a .env file.
BARD_KEY: Loads the Bard API key from the environment variables.

## 3. Setting Up Bard API Session

```python
session = requests.Session()
session.headers = {
    # Headers for the Bard API request
    # ...
}
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))
bard = Bard(session=session, timeout=30)
```
Sets up a session with specific headers for making requests to the Bard API.
Uses the Bard API key obtained from environment variables for authentication.

## 4. Speech-to-Text and Text-to-Speech Functions

```python
def SpeakText(command):
    # Function to convert text to speech using pyttsx3
    # ...

def record_text():
    # Function to record speech and convert it to text using Google's speech recognition
    # ...
```
SpeakText: Converts text to speech and plays the audio.
record_text: Records audio from the microphone, removes ambient noise, and converts speech to text.

## 5. Sending Requests to Bard API

```python
def send_to_bard(messages):
    # Function to send messages to the Bard API and receive responses
    # ...

messages = '''Initial Message for Bard before starting'''

```
send_to_bard: Sends messages to the Bard API using the Bard API instance and retrieves responses.
Set Initializing message

## 6. Main Loop

```python
while(1):
    # Main loop to interact with the user and Bard API
    # ...

```
Main loop to interact with the user by sending user messages to the Bard API and getting responses.

Sends the initial message to Bard API, receives a response, and converts it to speech using text-to-speech.
Interacts with the user by capturing speech and updating the messages variable accordingly
Allows the user to exit the virtual assistant by saying "sleep."
