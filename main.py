import eel
import speech_recognition as sr
import pyautogui
import keyboard
import pyttsx3

# Initialize Eel in the "web" folder
eel.init("web")

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, 0, 4)

    try:
        query = recognizer.recognize_google(audio, language='en-in')
        return query.lower()
    except Exception:
        return "none"

@eel.expose
def listen():
    command = takeCommand()
    response = handleCommand(command)
    return {"command": command, "response": response}

def handleCommand(query):
    if "volume up" in query:
        speak("Turning volume up")
        keyboard.send("volume up")
    elif "volume down" in query:
        speak("Turning volume down")
        keyboard.send("volume down")
    elif "pause" in query or "stop" in query:
        pyautogui.press("k")
        speak("Video paused")
    elif "play" in query:
        pyautogui.press("k")
        speak("Video played")
    elif "mute" in query:
        pyautogui.press("m")
        speak("Video muted")
    elif "forward" in query:
        pyautogui.press("l")
    elif "backward" in query or "back" in query:
        pyautogui.press("j")
    elif "exit" in query:
        speak("Exiting the program.")
        return "Exiting"
    else:
        return "Command not recognized."
    return f"Executed: {query}"



# Start the Eel app
eel.start("index.html", size=(400, 300), mode="chrome", port=8080)