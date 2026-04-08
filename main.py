import eel
import speech_recognition as sr
import pyautogui
import pyttsx3
import threading
import queue

# Initialize Eel
eel.init("web")

# TTS setup
engine = pyttsx3.init()
engine.setProperty("rate", 170)
speak_queue = queue.Queue()

def speak(audio):
    """Queue speech to avoid threading conflicts with pyttsx3"""
    speak_queue.put(audio)

def process_speech_queue():
    """Process queued speech in a safe manner"""
    while True:
        try:
            audio = speak_queue.get(timeout=0.1)
            engine.say(audio)
            engine.runAndWait()
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Speech error: {e}")

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        print("Listening...")
        audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except:
        return "none"


@eel.expose
def startListening():
    threading.Thread(target=listen_loop).start()

def listen_loop():
    while True:
        command = takeCommand()
        response = handleCommand(command)
        eel.updateUI(command, response)

def handleCommand(query):
    if "volume up" in query:
        speak("Turning volume up")
        pyautogui.press("volumeup")

    elif "volume down" in query:
        speak("Turning volume down")
        pyautogui.press("volumedown")

    elif "mute" in query:
        speak("Muting")
        pyautogui.press("volumemute")

    elif "pause" in query or "stop" in query:
        pyautogui.press("k")
        speak("Video paused")

    elif "play" in query:
        pyautogui.press("k")
        speak("Video playing")

    elif "forward" in query:
        pyautogui.press("l")

    elif "backward" in query or "back" in query:
        pyautogui.press("j")

    elif "exit" in query:
        speak("Exiting the program.")
        exit()

    else:
        return "Command not recognized."

    return f"Executed: {query}"

# Start app
# Start speech processing in background
speech_thread = threading.Thread(target=process_speech_queue, daemon=True)
speech_thread.start()

# Start Eel without close callback to avoid issues
eel.start("index.html", size=(400, 300), mode="chrome", port=8080)
