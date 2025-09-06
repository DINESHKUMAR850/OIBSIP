import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

speak("Hello, I am your Python Assistant. How can I help you?")

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello! How are you?")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
    
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    
    elif "search" in command:
        speak("What should I search for?")
        query = take_command()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the search results for {query}")
    
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        break
