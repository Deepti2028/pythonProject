
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def takecommand():
    try:
        with sr.Microphone() as source:
            print('Listening to you.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis','')
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = takecommand()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I :%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'what is a' in command:
        thing = command.replace('what is a','')
        info = wikipedia.summary(thing,2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry I dont like you')
    elif 'single' in command:
        talk('Yes I am busy overthrowing human race')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hey Hows your day?')
    elif 'jarvis are you there' in command:
        talk('At your service ')
    else:
        talk('Sorry I didnt get you.')
while True:
    run_jarvis()


