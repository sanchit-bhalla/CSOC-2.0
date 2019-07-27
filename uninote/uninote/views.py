from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse
import pyttsx3       # pip install pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser

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

def otp_form_view(request):
    form=forms.OtpForm()
    if request.method == 'POST':
        form=forms.OtpForm(request.POST)
    if form.is_valid():
        num = form.cleaned_data['Phone_number']
        with open("numbers.txt","a") as f:
            f.write(num+"\n")        

        import random
        import requests

        global rand_otp
        rand_otp = random.randint(1000,9999)
        url = "https://www.fast2sms.com/dev/bulk"
        querystring = {"authorization":"vwBj8nZfX1Ay2WUt6bLoGT7q5eRhYugKcisNzad0EM9lQVIP34g5dL2u1tFfvB4rSOnwDZXN3iAaVqbQ","sender_id":"FSTSMS","language":"english","route":"qt","numbers":f'{num}',"message":"13099","variables":"{BB}","variables_values":f'{rand_otp}'}
        headers = {
            'cache-control': "no-cache"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

        return redirect("confirm_otp")
    return render(request,'otp.html',{'form':form})

def confirm_otp_form_view(request):
    form = forms.ConfirmOtpForm()

    if request.method=="POST":
        form = forms.ConfirmOtpForm(request.POST)
    if form.is_valid():
        con_otp = form.cleaned_data['Confirm_OTP']
        if con_otp == str(rand_otp):
            return redirect('notes:choosedeptform')
        else:
            return redirect("otp")
    return render(request,'confirm_otp.html',{'form':form})

# making dictionary for operations to be performed on user's voice input
operations = {"sign up":'register_app:signup',"signup":'register_app:signup',

            "discussions":'discussions',"discuss":'discussions',"discussion":'discussions',
            "discussionform":'discussions',"q and a form":'discussions',"question and answer form":'discussions',

            "who create this":'about','creaters':'about','about this':'about',"open about":'about',"about page":'about',
            'creator':'about',"creators":'about',

            "show groups":'groups:all',"groups page":'groups:all',"all groups":'groups:all',"group list":'groups:all',
            "gorups list":'groups:all',"gourp list":'groups:all',"question answer":'groups:all',"questions and answers":'groups:all',

            "notes" : 'notes:homepage',"study material":'notes:homepage',"note":'notes:homepage',"departments":'notes:homepage',
            "department":'notes:homepage',

            'paper':'/papers/','papers':'/papers/','exams':'/papers/','exam':'/papers/'

            }

#  Operations for which login is necessary
login_operations = {
            "create group":'groups:create',"create groups":'groups:create',"new group":'groups:create',"new goups":'groups:create',
            "create a group":'groups:create',

            "create post":'posts:create',"create posts":'posts:create',"new post":'posts:create',"new posts":'posts:create',
            "question":'posts:create',"questions":'posts:create',"ask questions":'posts:create',"new question":'posts:create',
            'problems':'posts:create',"confusion":'posts:create','query':'posts:create','queries':'posts:create','doubt':'posts:create',
            'issue':'posts:create','issues':'posts:create','problem':'posts:create','doubts':'posts:crete',

}
superuser_op = {'upload':'otp','uploads':'otp','admin':'otp','permissions':'otp','add notes':'otp'}

depart ={

    'electronics':['Electronics','Technology'],'ece':['Electronics','Technology'],'electrical':['Electronics','Technology'],'electronic':['Electronics','Technology'],

    'btech':['Computer','Engineering'], 'cs':['Computer','Engineering'],'cse':['Computer','Engineering'],
    'computer science':['Computer','Engineering'], 'computer engineering':['Computer','Engineering'],'b tech':['Computer','Engineering'],
    'computerscience':['Computer','Engineering'],

}

sem={
    '1st':'first','1':'first','first':'first','2nd':'second','2':'second','second':'second','3rd':'third','3':'third','third':'third','4th':'fourth','4':'fourth',"fourth":'fourth','forth':'fourth',
    '5th':'fifth','5':'fifth','fifth':'fifth','6':'sixth','6th':'sixth','sixth':'sixth','7th':'seventh','7':'seventh','seventh':'seventh','8th':'eight','8':'eight'
}

subjects = {
    'electrical circiuts':'Electronics+Devices+and+Circuits','electronics devices':'Electronics+Devices+and+Circuits','circuits':'Electronics+Devices+and+Circuits',
    'electronic devices':'Electronics+Devices+and+Circuits','electrical devices':'Electronics+Devices+and+Circuits',

    'data communication':"Data+Communication",'datacommunication':'Data+Communication','dc notes':'Data+Communication','dc pdfs':'Data+Communication',

    'discrete mathematics':"Discrete+Mathematics",'discrete maths':"Discrete+Mathematics",'discrete mathematic':"Discrete+Mathematics",'discrete mas':"Discrete+Mathematics",
    'discrete math':"Discrete+Mathematics",'ds notes':"Discrete+Mathematics",'ds pdfs':"Discrete+Mathematics",

    'maths':"Maths",'math':"Maths",'mathematics':"Maths",'c':'C%2FC%2B%2B','cplusplus':'C%2FC%2B%2B','c plus plus': 'C%2FC%2B%2B','cplus plus':'C%2FC%2B%2B',
    'see plus plus':'C%2FC%2B%2B','sea plus plus':'C%2FC%2B%2B','see':'C%2FC%2B%2B','sea':'C%2FC%2B%2B'
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

    speak("How i help you?")

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
        return redirect("homepage")

    else:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        f = 0
        if f==0:
            for s in subjects:
                if s in query:
                    for d in depart:
                        if d in query:
                            dstr = ""
                            for ele in depart[d]:
                                dstr = dstr+ele+"+"
                            dstr = dstr[:len(dstr)-1]
                            for semester in sem:
                                if semester in query:
                                    if 'papers' in query or 'paper' in query or 'exam' in query or 'exams' in query:
                                        try:
                                            webbrowser.get(chrome_path).open_new_tab(f"http://127.0.0.1:8000/papers/displaypapers/?semester={sem[semester]}&subject={subjects[s]}&department={dstr}")
                                            f = 1
                                            break
                                        except:
                                            return redirect('/papers/')
                                    else:
                                        try:
                                            webbrowser.get(chrome_path).open_new_tab(f"http://127.0.0.1:8000/notes/displaynotes?semester={sem[semester]}&subject={subjects[s]}&department={dstr}")
                                            f = 1
                                            break
                                        except:
                                            return redirect('/notes/')
                            break
                    break
        if f==0:
            for q in superuser_op:
                if q in query:
                    f=1
                    if request.user.is_staff:
                        return redirect(superuser_op[q])
                    else:
                        speak("You do not have permissions for that!")
        if f==0:
            for k in operations:
                if k in query:
                    f = 2
                    return redirect(operations[k])

        if f==0:
            for k in login_operations:
                if k in query:
                    if request.user.is_authenticated:
                        return redirect(login_operations[k])
                    else:
                        speak("You need to login for that")
                        return redirect('register_app:login')

        return redirect("homepage")
