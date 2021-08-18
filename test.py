import speech_recognition as sr 
import playsound  
from gtts import gTTS 
import random
from time import ctime # 
import webbrowser  
import ssl
import certifi
import time
import datetime
import os 
from PIL import Image
import subprocess
import pyautogui  
import pyttsx3
import bs4 as bs
import urllib.request
import requests
import pywhatkit
import playsound
import pyscreenshot

class person:
    name = ''
    def setName(self, name):    
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

# def there_exists(terms):
#     for term in terms:
#         if term in voice_data:
#             return True

def speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()  
def get_audio(ask=""):
    with sr.Microphone() as source:  
        audio = r.listen(source, 5, 5)   
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) 
            print(voice_data) 
        except sr.UnknownValueError:  
            print('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down')  
        return voice_data.lower()

def speak(text):
    text = str(text)
    tts = gTTS(text=text, lang='en')  
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) 
    print(asis_obj.name + ":", text)  
    os.remove(audio_file)  

def respond(voice_data):
    text = get_audio()
    if 'are you there' in text:
        speak('I am online and ready Sir')
 
    if "what is your name" in text or "what's your name" in text or "tell me your name" in text:

        if person_obj.name:
            speak(f"My name is {asis_obj.name}, {person_obj.name}")  
        else:
            speak(f"My name is {asis_obj.name}. what's your name?")  

    if "my name is" in text:
        person_name = voice_data.split("is")[-1].strip()
        speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)  
    
    if "what is my name" in text:
        speak("Your name must be " + person_obj.name)
    
    if "your name should be" in text:
        asis_name = voice_data.split("be")[-1].strip()
        speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name)  

    if "how are you" in text or "how are you doing" in text:
        speak("I'm very well, thanks for asking " + person_obj.name)

    if "what's the time" in text or "tell me the time" in text or "what time is it" in text or"what is the time" in text:
        d = datetime.datetime.now().strftime("%I:%M:%p" )   
        speak(f"the time is {d}")

    if "search for" in text and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for" + search_term + "on google")
    
    if "search" in text and 'youtube' not in voice_data:
        search_term = voice_data.replace("search","")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for" + search_term + "on google")

    if "youtube" in text:
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for " + search_term + "on youtube")

    if "price of" in text:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        speak("Here is what I found for " + search_term + " on google")

    if 'play' in text:
        song = voice_data.split('play')[-1]
        speak('playing ' + song)
        pywhatkit.playonyt(song)

    if "question" in text:
        #playsound.playsound('start.mp3')
        try:
            question = voice_data.split('question')[-1]
            app_id = 'GT6KVX-23HU3T98T6'
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        except  Exception as e:
            speak("Sorry, I don't know that")    

    if "weather" in text:
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        speak("Here is what I found for on google")

    if "toss" in text or "flip" in text or "coin" in text:
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        speak("The computer chose " + cmove)
        
    if "capture" in text or "my screen" in text or "screenshot" in text or "take a screenshot" in text:
        #playsound.playsound('start.mp3')
        image = pyscreenshot.grab()
        speak('What do you want me to name it')
        ans = get_audio()
        image.save(ans+'.jpg')
        speak('done')

    if "exit" in text:
        speak("Going offline")
        exit()

    if "what is my exact location" in text:
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        speak("You must be somewhere near here, as per Google maps")

time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Pixel'
person_obj.name = ""
engine = pyttsx3.init()


while True:
    voice_data = get_audio("Recording") # get the voice input
    #print("Done")
    #print("Q:", voice_data)
    respond(voice_data) # respond

