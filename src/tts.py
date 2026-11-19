import os
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# Project paths
BASE_DIR = Path(__file__).resolve().parent

# Load API key from root .env
load_dotenv(BASE_DIR.parent / ".env")

api_key = os.getenv("ELEVENLABS_API_KEY")

client = ElevenLabs(api_key=api_key)

# Read text from file
text_file = BASE_DIR / "data" / "input.txt"

with open(text_file, "r", encoding="utf-8") as file:
    text = file.read()

# Convert text into speech
audio = client.text_to_speech.convert(
    text=text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

# Save generated audio
output_file = BASE_DIR / "data" / "output.mp3"

with open(output_file, "wb") as audio_file:
    for chunk in audio:  # noqa: FURB122
        audio_file.write(chunk)

print(f"Audio generated successfully: {output_file}")
