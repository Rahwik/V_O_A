import pyttsx3 
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import os
import webbrowser

# Initialize speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()

# Configure the speech engine properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# Function to speak out the provided text
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('Command:', command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return ""
    except Exception as e:
        print(f"An error occurred in take_command: {e}")
        return ""

# Function to greet user based on current time
def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 3 <= hour < 12:
        talk('Good morning sir!')
    elif 12 <= hour < 18:
        talk('Good afternoon sir!')
    else:
        talk('Good evening sir!')

# Function to handle various commands
def run_jarvis():
    command = take_command()
    if 'hello' in command or 'namaste' in command:
        # Greeting
        talk('Hi boss, how are you?')
    elif 'joke' in command:
        # Fetch and tell a joke
        talk(pyjokes.get_joke())
    elif 'play' in command:
        # Play a song on YouTube
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        # Tell the current time
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print('Current time:', current_time)
        talk(current_time)
    elif 'open' in command:
        # Open a specified application
        command = command.replace('open', '')
        pyautogui.press('super')
        pyautogui.typewrite(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        talk('opening ' + command)
    elif 'close' in command:
        # Close the active window
        talk('Closing Sir!')
        pyautogui.hotkey('alt','f4')
    elif 'who is' in command:
        # Fetch information about a person from Wikipedia
        person = command.replace('who is','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'remember that' in command:
        # Remember a message from the user
        rememberMessage = command.replace('remember that', '')
        talk('you told me to remember that ' + rememberMessage)
        remember = open('remember.txt', "a")
        remember.write(rememberMessage)
        remember.close()
    elif "what do you remember" in command:
        # Retrieve and tell the remembered message
        remember = open('remember.txt', 'r')
        talk('you told me to remember ' + remember.read())
    elif "clear remember file" in command:
        # Clear the remember file
        file = open('remember.txt', 'w')
        file.write(f"")
        talk('done everything I remember has been deleted.')
    elif 'shutdown' in command:
        # Shutdown the computer
        talk('closing the pc in')
        talk('3. 2. 1')
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        # Restart the computer
        talk('restarting the pc in')
        talk('3. 2. 1')
        os.system("shutdown /r /t 1")
    elif "search" in command:
        # Search the internet
        usercm = command.replace("search", "")
        usercm = usercm.lower()
        webbrowser.open(f"{usercm}")
        talk('this is what I found on the internet')
    elif "stop" in command or "start" in command:
        # Stop or start a process
        pyautogui.press('k')
        talk('done')
    elif "full screen" in command:
        # Toggle fullscreen mode
        pyautogui.press('f')
        talk('done')
    else:
        # Default response
        talk("I do not understand")

# Main function
if __name__ == "__main__":
    greeting()
    try:
        while True:
            run_jarvis()
    except KeyboardInterrupt:
        print("Program terminated by user")
