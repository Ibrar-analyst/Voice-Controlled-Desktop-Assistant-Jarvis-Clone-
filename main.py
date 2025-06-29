import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

from gtts import gTTS
import pygame
import os

pygame.mixer.init()
engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")



def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif command.lower().startswith("play"):
        try:

            song = command.lower().split(" ")[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
        except KeyError:
            speak(f"Sorry, I couldn't find the song {song}.")
    else:
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            r = sr.Recognizer()


            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening for wake word...")
                # 2,1
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("yes boss")

                with sr.Microphone() as source:
                    print("Jarvis is active. Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
