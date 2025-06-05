FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

RUN pip install TTS==0.22.0
RUN pip install transformers==4.36.2
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install python-multipart
RUN pip install aiofiles
RUN pip install soundfile
RUN pip install numpy

WORKDIR /app
COPY main.py .

CMD ["python3", "main.py"]
