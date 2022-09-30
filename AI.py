import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint


master = 'Saurabh'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back " + master)
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    # speak("the current Time is")
    # speak(Time)
    # speak("the current Date is")
    # speak(date)
    # speak(month)
    # speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning " + master)

    elif hour>=12 and hour<18:
        speak("Good Afternoon " + master)

    elif hour>=18 and hour<24:
        speak("Good Evening " + master)

    else:
        speak("Good Night" + master)

    speak("Jarvis at your Service. Please tell me how can I help You ")
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Saurabh Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', 'senderpassword')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('google think you said:\n' +text +'.com')
                wb.get(chrome_path).open(text+'.com')
            except Exception as e:
                print(e)


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'email to Saurabh' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "senderemail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")      

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\user account\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"#ADD THE PATH OF THE PROGEM HERE
        #     os.startfile(codePath)


        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))




        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()

        
