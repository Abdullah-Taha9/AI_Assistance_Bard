import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from bardapi import Bard
import requests


load_dotenv()
BARD_KEY = os.getenv('BARDKEY')
os.environ["_BARD_API_KEY"] = BARD_KEY


# Continuing the conversation using a reusable session, without setting new conversation.
session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
bard = Bard(session=session, timeout=30)


# Converting Text to Speech, "Bard responses"
def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()


# Speech to Text, "Microphone Input"
def record_text():
 
    while(1):

        try:

            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("I'm listening")
                audio2 = r.listen(source2)
                MyText =r.recognize_google(audio2)
                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unkown error occured")


# Send requests to Bard
def send_to_bard(messages):

    response = bard.get_answer(messages)['content']
    return response

messages = '''Hi, Act like you are my virtual assistance, keep your resoponse as you are speaking, not writing.
              If you understand say only (Hi engineer Abdullah, I am tasker, your virtual assistance, How can I help you today)'''


# Main
while(1):

    response = send_to_bard(messages)
    if response.find('*'):
        response = response.replace('*', '')
    SpeakText(response)
    print(response)
    text = record_text()
    if text.find('sleep') != -1: break
    messages = text + "(only give a very brief answer)"
    print(messages)