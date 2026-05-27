import torch
from transformers import pipeline
import os
import time


AUDIO_FILE = "data/sample_audios/NDA/AmitShahLakhisarai.wav"
MODEL_NAME = "openai/whisper-medium"
# "openai/whisper-small"
# "openai/whisper-large-v3"
# "vasista22/whisper-hindi-large-v2"
LANGUAGE = "hi"
OUTPUT_FOLDER = "data/transcripts/NDA"

device = 0 if torch.cuda.is_available() else -1
print(f"\nUsing Device: {'GPU' if device == 0 else 'CPU'}")

print("\nLoading Whisper model...")

pipe = pipeline(
    task="automatic-speech-recognition",
    model=MODEL_NAME,
    chunk_length_s=30,
    device=device
)

print("Model Loaded Successfully!")

print("\nStarting transcription...\n")

start_time = time.time()
result = pipe(
    AUDIO_FILE,
    generate_kwargs={
        "language": LANGUAGE,
        "task": "transcribe"
    },
    return_timestamps=True
)

end_time = time.time()

print(result["text"])
print(f"Transcription Time: {end_time - start_time:.2f} seconds")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
audio_name = os.path.splitext(os.path.basename(AUDIO_FILE))[0]

output_path = os.path.join(
    OUTPUT_FOLDER,
    f"{audio_name}_transcript.txt"
)

with open(output_path, "w", encoding="utf-8") as f:

    f.write(result["text"])

print(f"\nTranscript saved to:\n{output_path}")

if "chunks" in result:

    timestamp_file = os.path.join(
        OUTPUT_FOLDER,
        f"{audio_name}_timestamps.txt"
    )

    with open(timestamp_file, "w", encoding="utf-8") as f:

        for chunk in result["chunks"]:

            timestamp = chunk["timestamp"]
            text = chunk["text"]

            line = f"[{timestamp[0]} --> {timestamp[1]}] {text}\n"

            f.write(line)

    print(f"\nTimestamps saved to:\n{timestamp_file}")