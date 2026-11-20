# Voice Chatbot – Text-to-Speech (TTS) & Speech-to-Text (STT)

This project demonstrates two basic voice-processing tasks using **ElevenLabs** and **Deepgram**.

- **Text-to-Speech (TTS):** Converts text from a local `.txt` file into spoken audio.
- **Speech-to-Text (STT):** Converts speech from a local audio file into readable text.

## 1. Project Structure

```text
voice_chatbot/
│
├── .env
├── .gitignore
├── requirements.txt
│
└── src/
    ├── tts.py
    ├── stt.py
    │
    └── data/
        ├── input.txt
        ├── output.mp3
        └── dragons.wav
```

## 2. Installation and Setup

### Step 1: Create and activate a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API keys

Keep your API keys private. Do not upload the `.env` file to GitHub.

---

## 3. Text-to-Speech (TTS) – ElevenLabs

### How it works

Text-to-Speech converts written text into spoken audio.

1. The `tts.py` script reads the text from the local file `src/data/input.txt`.
2. The text is sent to the ElevenLabs Text-to-Speech API.
3. ElevenLabs processes the text using the selected voice and TTS model.
4. The API generates audio data.
5. The script receives the generated audio and writes it to an MP3 file.

### Workflow

```text
input.txt
    |
    v
Read text from local file
    |
    v
ElevenLabs TTS API
    |
    v
Generate speech audio
    |
    v
Save generated audio
    |
    v
src/data/output.mp3
```

### How to run

From the project root directory, execute:

```bash
python src/tts.py
```

### Output

After successful execution, the generated speech is saved at:

```text
src/data/output.mp3
```

You can open the MP3 file using any audio player to listen to the generated speech.

---

## 4. Speech-to-Text (STT) – Deepgram

### How it works

Speech-to-Text converts spoken audio into written text.

In this task, a prerecorded audio file is provided locally.

1. The `stt.py` script opens the local audio file `src/data/dragons.wav`.
2. The script reads the audio file in binary format.
3. The audio data is sent to the Deepgram Speech-to-Text API.
4. Deepgram processes and recognizes the spoken words in the audio.
5. Deepgram returns the recognized speech as a text transcript.
6. The script extracts and prints the transcript in the terminal.

### Workflow

```text
dragons.wav
    |
    v
Read local audio file
    |
    v
Send audio data to Deepgram
    |
    v
Deepgram STT processing
    |
    v
Generate text transcript
    |
    v
Display transcript in terminal
```

### How to run

From the project root directory, execute:

```bash
python src/stt.py
```

### Output

The recognized text is displayed directly in the terminal.

**Note:** In the current implementation, the transcript is printed but is not saved to a separate text file.

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| ElevenLabs | Text-to-Speech conversion |
| Deepgram | Speech-to-Text conversion |
| python-dotenv | Loads API keys from the `.env` file |
| pathlib | Handles project and file paths |

## 6. Important Notes

- TTS uses a local text file as input and generates an MP3 audio file.
- STT uses a local WAV audio file as input and returns its recognized text.
- Both tasks use API-based processing, so an internet connection and valid API keys are required.
- These implementations process prerecorded files; they do not yet support live microphone input or real-time audio streaming.

## 7. Run Commands Summary

Run these commands from the project root:

```bash
# Generate speech from text
python src/tts.py

# Convert audio speech into text
python src/stt.py
```
