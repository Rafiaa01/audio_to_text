
import os
from pathlib import Path

from deepgram import DeepgramClient
from dotenv import load_dotenv

# Locate project directories
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables
load_dotenv(BASE_DIR.parent / ".env")

api_key = os.getenv("DEEPGRAM_API_KEY")

if not api_key:
    raise ValueError("DEEPGRAM_API_KEY not found!")

# Initialize Deepgram
client = DeepgramClient(api_key=api_key)

# Locate audio file
audio_file_path = BASE_DIR / "data" / "dragons.wav"

# Send audio to Deepgram
with open(audio_file_path, "rb") as audio_file:
    response = client.listen.v1.media.transcribe_file(
        request=audio_file.read(),
        model="nova-3",
        smart_format=True
    )

# Extract transcript
transcript = (
    response.results.channels[0]
    .alternatives[0]
    .transcript
)

print("Transcribed Text:")
print(transcript)
