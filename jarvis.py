import pyttsx3
import pyaudio
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 250)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print(sr.Microphone.list_microphone_names())
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except Exception as e:
        print(f"An error occurred in take_command: {e}")
        return ""

def run_jarvis():
    command = take_command()
    if 'hello' in command:
        talk('hi boss how are you')

talk('hello world')

while True:
    run_jarvis()
