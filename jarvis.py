import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser  
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
     
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how May I help you")

def takecommand():
    #it takes microphones input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)
        print("say that again please...")
        speak("say that again please...")
        return "None"
    return query
    



if __name__ == "__main__":
    wishme()
    
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'google' in query:
            webbrowser.open('google.com')
        
        elif 'hackerrank' in query:
            webbrowser.open('hackerrank.com')
        
        elif 'stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'stock market' in query:
            webbrowser.open('https://www.investing.com/')

        elif ' open zoom'  in query:
            webbrowser.open('https://zoom.us/meetings')

        elif 'play music' in query:
            music_dir = 'F:\\music\\new hits'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'my father' in query:
            speak('hey rishabh !. your fathers name is  manoj kumar jain. he is a businessman and a hardworking personality . ')

        elif 'visual studio' in query:
            codepath = "C:\\Users\\LENOVO\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)

        elif ' open gmail' in query:
            webbrowser.open('https://mail.google.com/')
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        

