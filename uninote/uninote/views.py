from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.urls import reverse
import pyttsx3       # pip install pyttsx3
import datetime
import speech_recognition as sr
import os

class Homepage(TemplateView):
    template_name = 'homepage.html'


class Test(TemplateView):
    template_name = 'test.html'

class Thanks(TemplateView):
    template_name = 'thanks.html'

class About(TemplateView):
    template_name = 'about.html'

class Discussions(TemplateView):
    template_name = 'discussions.html'

class Response(TemplateView):
    template_name = 'response.html'

# making dictionary for operations to be performed on user's voice input
operations = {"sign up":'register_app:signup',"signup":'register_app:signup',

            "discussions":'discussions',"discuss":'discussions',"discussion":'discussions',
            "discussionform":'discussions',"q and a form":'discussions',"question and answer form":'discussions',

            "who create this":'about','creaters':'about','about this':'about',"open about":'about',"about page":'about',

            "show groups":'groups:all',"groups page":'groups:all',"all groups":'groups:all',"group list":'groups:all',
            "gorups list":'groups:all',"gourp list":'groups:all',"question answer":'groups:all',"questions and answers":'groups:all',

            "create group":'groups:create',"create groups":'groups:create',"new group":'groups:create',"new goups":'groups:create',
            "create a group":'groups:create',

            "create post":'posts:create',"create posts":'posts:create',"new post":'posts:create',"new posts":'posts:create',
            "question":'posts:create',"questions":'posts:create',"ask questions":'posts:create',"new question":'posts:create',
            'problems':'posts:create',"confusion":'posts:create','query':'posts:create','queries':'posts:create',
            'issue':'posts:create','issues':'posts:create','problem':'posts:create',

            }
def speak(audio):
    engine = pyttsx3.init('sapi5')  # sapi5 is used for voices
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)  # use 0 for male voice
    engine.say(audio)
    engine.runAndWait()

def Ask(request):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Aleska speaking!. How i help you?")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # You can change other parameters according to your requirements
        audio = r.listen(source)
    try:
        print("Recognising...")
        # instead of google you can use some other also
        query = r.recognize_google(audio, language='en-in')  #en-in --> english-india
        print(f"user said: {query}\n")
        query = query.lower()

    except Exception as e:
        print(e)
        speak("Say that again please ...")

    else:
        for k in operations:
            if k in query:
                return redirect(operations[k])
        return redirect("homepage")
