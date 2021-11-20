import speech_recognition as sr
import pyttsx3
import requests
import urllib
import json

r = sr.Recognizer()
engine = pyttsx3.init()
engine.say("I am ready")
engine.runAndWait()
no = 1
ain = "suha"
while no == 1:
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
         out = r.recognize_google(audio)
         if out != "":
             no = 1 - 1
             print(no)
             if out.find(ain) != -1:
                 engine.say("How can I help?")
                 engine.runAndWait()
             elif no == 0:
                 encoded = urllib.parse.quote("hey", safe='')
                 url = "https://api.pgamerx.com/v3/ai/response?message=" + encoded + "&language=en&dev_name=Jay&bot_name=suha&type=stable&unique_id=1"

                 response = requests.request("GET", url, headers={'x-api-key': 'PMhOCKLnEP8v'})
                 json1 = response.json()

                 jsony = json.dumps(json1)
                 res = jsony.split('"')
                 engine.say(res[5])
                 engine.runAndWait()



        except:
            no = 1
            print(no)

