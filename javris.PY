import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
import pyautogui
from plyer import notification
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am jarvis your personal assistant.How can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def make_request(url):
  response = requests.get(url)
  return response.text

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        #elif 'open google' in query:
            #webbrowser.open("google.com")

        elif 'open stack' in query:
            webbrowser.open("stackoverflow.com")



        elif 'open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Tanishk\\Music\\New folder\\musical things'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)

        elif 'open website' in query:
            speak(
                "Please type the name of the website that you want to open (specify the full url) \n")
            website_name = input()
            print(website_name)
            webbrowser.get(
                'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(website_name)
            speak(f"{website_name} opened.")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')

        elif 'covid stats' in query:
            html_data = make_request('https://www.worldometers.info/coronavirus/')
            # print(html_data)
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            print('total cases : ', total_cases)
            print('new cases', new_cases[1:])
            print('total recovered', total_recovered)
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
                title="COVID-19 Statistics",
                message=notification_message,
                timeout=5
            )
            speak("here are the stats for COVID-19")


        elif 'open code' in query:
            codePath = "D:\python\PYTHON First course"
            os.startfile(codePath)

        elif 'email to Tanishk' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Tanishk bhai. I am not able to send this email")    
