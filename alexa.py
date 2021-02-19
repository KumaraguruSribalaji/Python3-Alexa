import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener= sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

engine.say('I am your alexa')
engine.say('What can i do for YOU!')
engine.runAndWait()

def action():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa' , '')
                print(command)
    except:
        pass
    return command


def  run_alexa():
    command = action()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is' + time )
        print(time)
        talk('Current time is ' + time)
    elif 'Wikipedia' in command:
        person = command.replace('Wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('please say it again!!.')

while True:
    run_alexa()