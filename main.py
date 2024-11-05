import speech_recognition as sr
import pyautogui
import keyboard
import pyttsx3

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
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception:
        print("Say that again, please.")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "volume up" in query:
            speak("Turning volume up, sir")
            keyboard.send("volume up")
        elif "volume down" in query:
            speak("Turning volume down, sir")
            keyboard.send("volume down")
        elif "pause" in query:
            pyautogui.press("k")
            speak("Video paused")
        elif "stop" in query:
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
        elif "backward" in query:
            pyautogui.press("j")
        elif "back" in query:
            pyautogui.press("j")
        elif "exit" in query:
            speak("Exiting the program.")
            break