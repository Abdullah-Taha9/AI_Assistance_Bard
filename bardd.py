# Python Program (Speech to text and text to speech) using Google Bard
# Indepedndies
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from bardapi import Bard
import requests
load_dotenv()
BARD_KEY = os.getenv('BARDKEY')
os.environ["_BARD_API_KEY"] = 'bgjtNLLJ_LS5vgu0myOd9rUip29SRbY9eGeU6c33DZrftrhh7GvkRZzydePHNOgrnkIxpw.'
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
# session.cookies.set("__Secure-1PSID", token) 

bard = Bard(session=session, timeout=30)



#Function to convert text to speech
def SpeakText(command):
    
    #Initialize the engine
    engine = pyttsx3.init()
    # Give it the text we want it to say
    engine.say(command)
    #run the above command and say the text
    engine.runAndWait()

#installiing the recognizer
r = sr.Recognizer()

def record_text():
# loop in case of errors    
    while(1):
        try:
            # use the microphone as source of input
            with sr.Microphone() as source2:

                # prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("I'm listening")

                #listen for the user's input
                audio2 = r.listen(source2)


                # Using google to recognize audio
                MyText =r.recognize_google(audio2)

                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unkown error occured")


def send_to_bard(messages):

  """Sends a message to Bard and returns the response.

  Args:
    messages: A list of messages that make up the conversation context.

  Returns:
    A string containing the response from Bard.
  """

  # Create a BardAPI object.
#   bard_api = Bard()

#   import pdb
#   pdb.set_trace()


  # Query Bard with the given messages.
  response = bard.get_answer(messages)['content']

  # Get the response text.
  response_text = response

  # Return the response text.
  return response_text


messages = "Hi engineer Abdullah Taha, I am tasker, your virtual assistance, how can I help you"

while(1): #infinite loop

    #This funcion convert the microphon audio and return the a text version from this audio in a form of string
    text = record_text()
    # if "quit" in text:
    #     break
    if text.find('quit') != -1: break

    #append the text recieved to the as a dictionary, to keep track of the whole conversation when talk again and respond accordingly
    # "role" is to identifiy who said that text
    messages = text + "(only give a very brief answer)"
    print(messages)
    
    #send message to chatGPT, and recive the response from chatgpt and convert it to audio
    response = send_to_bard(messages)
    SpeakText(response) #speak the text back to user
    print(response)