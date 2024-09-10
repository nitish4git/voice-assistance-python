import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listerner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Speak>>>')
            voice = listerner.listen(source)    
            command = listerner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return  command

def run_alexa():

    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'love' in command:
        talk("I'm in relationship with developer")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Sorry Can't Understand")

while True:
    run_alexa()