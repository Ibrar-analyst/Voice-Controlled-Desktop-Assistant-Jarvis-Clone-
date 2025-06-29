# 🚀 Voice-Controlled Desktop Assistant (Jarvis Clone)

## 🎤 Project Overview

A Python-based **Voice-Controlled Desktop Assistant** inspired by Jarvis from Iron Man. This assistant listens for the wake word **"Jarvis"**, accepts voice commands, and performs automated tasks like:

* Opening popular websites
* Playing music from a predefined library
* Providing real-time voice responses using text-to-speech (TTS)

This project demonstrates **real-time voice interaction, web automation, and audio playback** using Python libraries.

---

## 🔧 Features

* ✅ Wake word detection ("Jarvis")
* ✅ Voice command processing
* ✅ Opens Google, YouTube, Facebook, LinkedIn via voice
* ✅ Custom music playback using a predefined library
* ✅ Voice responses with `gTTS` and `PyGame`
* ✅ Robust error handling and continuous listening loop

---

## 🛠️ Technologies Used

* **Python 3**
* **SpeechRecognition** – Voice input processing
* **gTTS (Google Text-to-Speech)** – Voice output generation
* **PyGame** – Audio playback management
* **pyttsx3** – Offline text-to-speech engine
* **Webbrowser** – Automated website launching
* **Pyperclip** – Clipboard operations (if extended)

---

## 🚀 How to Run

### Prerequisites:

* Python 3 installed
* Microphone connected
* Internet connection (for gTTS and Google Speech Recognition)

### Installation:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install gTTS
pip install pygame
pip install pyperclip
```

### Run the Assistant:

```bash
python jarvis_assistant.py
```

### 📢 Usage:

1. The assistant will listen for the wake word **"Jarvis"**.
2. Upon detecting the wake word, it will become active and prompt you for a command.
3. Supported commands:

   * `open google`
   * `open youtube`
   * `open facebook`
   * `open linkedin`
   * `play <song_name>` (song must be present in the `musicLibrary` dictionary)

---

## 💡 Example Commands:

* "Jarvis" (wake word)
* "Open Google"
* "Open YouTube"
* "Play shapeofyou"

---

## ⚙️ Project Structure

```text
|-- jarvis_assistant.py
|-- musicLibrary.py
```

> Note: You should define the music links in `musicLibrary.py` in this format:

```python
music = {
    "shapeofyou": "https://link_to_song.com",
    "song2": "https://link_to_song.com"
}
```

---

## 🚀 Future Improvements

* Add more dynamic conversation capabilities.
* Implement offline voice recognition.
* Extend functionality to control system apps.
* Add GUI interface for better usability.

---

## 🙌 Acknowledgments

* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [gTTS](https://pypi.org/project/gTTS/)
* [PyGame](https://www.pygame.org/)
* [pyttsx3](https://pypi.org/project/pyttsx3/)

---

