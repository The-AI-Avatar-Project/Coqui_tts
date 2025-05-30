#!/bin/bash

# test_clone.sh – Erzeugt eine Stimme mit Sprachklonung durch eigenes Docker-Image

TEXT="Guten Tag! Ich bin Professor KI."
SPEAKER="prof1"
SAMPLE_PATH="samples/${SPEAKER}.wav"
OUTPUT="output/${SPEAKER}_klon.wav"

echo "[INFO] Starte Sprachklonung mit $SAMPLE_PATH..."
mkdir -p output

docker run --rm \
  -v "$(pwd)/output:/output" \
  -v "$(pwd)/samples:/samples" \
  coqui-tts-custom \
  --text "$TEXT" \
  --speaker_wav "/samples/${SPEAKER}.wav" \
  --out_path "/output/$(basename $OUTPUT)"

echo "[FERTIG] Geklonte Datei gespeichert unter: $OUTPUT"