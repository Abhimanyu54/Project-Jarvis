import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicCollection
import google.generativeai as genai
import time


def speak(Text):
             print(f"Jarvis: {Text}")
             engine = pyttsx3.init()
             voices = engine.getProperty('voices')
             engine.setProperty('voice',voices[0].id)
             engine.setProperty('rate',150)
             engine.setProperty('volume',1.0)
             engine.say(Text)
             engine.runAndWait()

def aiprocess(command):
    genai.configure(api_key="AIzaSyB_SP4axHAX52WWj7lquEPZeCWxe52o-k0")
    model = genai.GenerativeModel(model_name="models/gemma-3-1b-it")
    response = model.generate_content(command)
    return response.text
     

     
def processCommand(c):
        

        if "open google" in c.lower():
            webbrowser.open("https://www.google.com/")


        elif "open youtube" in c.lower():
            webbrowser.open("https://www.youtube.com/")


        elif "open instagram" in c.lower():
            webbrowser.open("https://www.instagram.com/")


        elif "open linkedin" in c.lower():
             webbrowser.open("https://in.linkedin.com/")


        elif c.lower().startswith("play"):
             song = c.lower().split(" ")[1]
             Link = MusicCollection.music[song]
             webbrowser.open(Link)

        else:
                output = aiprocess(c)
                print("Answer from AI: ", output)
                speak(output)
                time.sleep(1)





if __name__ == '__main__':
        
        speak ("Yo bro what's up, Need anything?")

        while True:

            r = sr.Recognizer()
            print("recognizing....")

            try:
                with sr.Microphone() as source: 
                    print("Listening...")
                    audio = r.listen(source, timeout=20, phrase_time_limit=20)
                word = r.recognize_google(audio)
                if (word.lower() == "jarvis"):
                    speak("ya")
                    time.sleep(1)
                    with sr.Microphone() as source:
                         print("Jarvis Active....")
                         audio = r.listen(source)
                         command = r.recognize_google(audio)
                         print ("You said:", command)
                         processCommand(command)
            except Exception as e:
                print("Error; {0}".format(e))
