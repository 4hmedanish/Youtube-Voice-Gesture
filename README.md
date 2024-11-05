# Youtube-Voice-Gesture
This Python script provides voice command functionality to control media playback and volume on your computer. It leverages speech_recognition for capturing and interpreting spoken commands, pyautogui and keyboard for media control, and pyttsx3 for providing audio feedback to the user.

Features:
Voice Recognition: Captures and processes voice commands using Google’s speech recognition API.
Media Control: Supports playback control (play, pause, mute, forward, backward) and volume adjustments.
Audio Feedback: Provides spoken feedback for each action using pyttsx3.

Requirements:
Python packages: speech_recognition, pyttsx3, pyautogui, keyboard.
Ensure that the necessary microphone and speaker configurations are set up.

How to Use:
Run the script.
Speak one of the supported commands, such as "volume up," "pause," or "exit."
The program will respond to your commands until you say "exit."
