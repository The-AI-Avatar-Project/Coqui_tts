# How to run it
## Build the Dockerfile locally and generate voice

```bash
docker build -t synesthesiam/coqui-tts .

##And run it with

```bash
python test.py

##To clone a voice run:

```bash
docker build -t coqui-tts-custom .

##And run it with

```bash
python test_clone.py
