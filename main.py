from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from TTS.api import TTS
import os
import uuid
import shutil
import torch

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = "profiles"
os.makedirs(BASE_DIR, exist_ok=True)


device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)


@app.post("/clone")
async def clone_voice(user_id: str = Form(...), audio: UploadFile = File(...)):
    user_dir = os.path.join(BASE_DIR, user_id)
    os.makedirs(user_dir, exist_ok=True)

    voice_path = os.path.join(user_dir, "voice.wav")
    with open(voice_path, "wb") as f:
        shutil.copyfileobj(audio.file, f)

    return {"message": f"Voice cloned for user '{user_id}'", "path": voice_path}


@app.post("/speak")
async def speak(user_id: str = Form(...), text: str = Form(...), language: str = Form(...)):
    user_dir = os.path.join(BASE_DIR, user_id)
    voice_path = os.path.join(user_dir, "voice.wav")

    if not os.path.isfile(voice_path):
        raise HTTPException(status_code=404, detail="Voice not found for this user.")

    output_path = os.path.join(user_dir, f"spoken_{uuid.uuid4().hex}.wav")

    try:
        tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker_wav=voice_path,
            language=language
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {e}")

    return FileResponse(output_path, media_type="audio/wav", filename="output.wav")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
