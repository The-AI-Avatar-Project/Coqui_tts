 Avatar KI – Sprachsynthese & Voice Cloning mit Coqui TTS

Dieses Projekt erzeugt Audiodateien aus Text und kann Stimmen anhand von Sprachproben klonen – alles über Docker ausführbar.

 Hauptfunktionen
Text-zu-Sprache (TTS) mit `synesthesiam/coqui-tts`
Stimmenklonung über ein eigenes Docker-Image

1. Sprachsynthese (Text → Stimme)
Verwendetes Image: `synesthesiam/coqui-tts`

```bash
python test.py

##➡ Erstellt output/voix.wav aus dem eingegebenen Text.

3. Stimmenklonung (Beispielstimme + Text → geklonte Stimme)
Eigenes Docker-Image erstellen:##

```bash
docker build -t coqui-tts-custom .


##Test ausführen:##

```bash
python test_clone.py

##➡ Nutzt samples/professeur.wav, um eine geklonte Stimme in output/ zu generieren.



 Beispiel (Python-Aufruf):##

```python
from scripts.generate_voice import generiere_stimme
generiere_stimme("professeur", "Guten Tag zusammen.")

```python
from scripts.generate_voice_clone import voix_clone
voix_clone("professeur", "Heute lernen wir etwas über künstliche Intelligenz.")
 Ergebnisse

##Alle generierten .wav-Dateien befinden sich im Ordner output/.

Voraussetzungen
Docker
Python 3.x##
