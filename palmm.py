from google.generativeai.types.discuss_types import MESSAGE_PROMPT_KEYS
import pprint
import google.generativeai as palm
import speech_recognition as sr
import pyttsx3
import os
PALM_KEY = os.getenv('PALMKEY')
palm.configure(api_key=PALM_KEY)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

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

messages = ""

def send_to_bard(messages):

  completion = palm.generate_text(
      model=model,
      prompt=messages,
      temperature=0,
      # The maximum length of the response
      max_output_tokens=100,
  )
  response_text = completion.result
  return response_text

# messages = "Hi engineer Abdullah Taha, I am tasker, your virtual assistance, how can I help you"

while(1): #infinite loop
    

    #This funcion convert the microphon audio and return the a text version from this audio in a form of string
    text = record_text()
    # if "quit" in text:
    #     break
    if text.find('quit') != -1: break

    #append the text recieved to the as a dictionary, to keep track of the whole conversation when talk again and respond accordingly
    # "role" is to identifiy who said that text
    messages = text + " (Keep the answer not more than 20 words)"
    print(messages)
    
    
    #send message to chatGPT, and recive the response from chatgpt and convert it to audio
    response = send_to_bard(messages)
    SpeakText(response) #speak the text back to user
    print(response)

    