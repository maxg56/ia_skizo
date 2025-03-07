from gtts import gTTS
import os

def speak(text, lang="fr"):
    tts = gTTS(text=text, lang=lang)
    tts.save("test.mp3")
    os.system("mpg123 test.mp3")
    os.remove("test.mp3")

if __name__ == "__main__":
    speak("Bonjour, ceci est un test.")
