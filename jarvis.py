import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('hello world i am the first ai created')