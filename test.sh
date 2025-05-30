#!/bin/bash

# Chemin absolu correct vers le dossier output
OUTPUT_DIR=$(pwd)/output

# Crée le dossier s’il n’existe pas
mkdir -p "$OUTPUT_DIR"

echo "[INFO] Starte einfache Text-zu-Sprache-Synthese..."

docker run --rm \
  -v "$OUTPUT_DIR":/output \
  synesthesiam/coqui-tts \
  --text "Hallo! Das ist ein Test der generierten Stimme." \
  --out_path /output/test_normal.wav

echo "[FERTIG] Datei gespeichert unter: output/test_normal.wav"