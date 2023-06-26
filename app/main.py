import sys
from fastapi import FastAPI
from fastapi import Response
from pydantic import BaseModel
from bark import SAMPLE_RATE, generate_audio, preload_models


app = FastAPI()
version = "{0}.{1}".format(sys.version_info.major, sys.version_info.minor)


class Text(BaseModel):
    text: str


@app.on_event("startup")
async def startup_event():
    app.state.model = None


@app.get("/")
async def index():
    return "Suno AI - Bark with FastAPI app running on Hypercorn and Python {}.".format(version)


@app.post("/generate")
def generate(text: Text):
    print(f"Data received: {text.text}")
    assert text != "", "Empty string!"
    print("Preloading models...")
    preload_models()
    print("Done.")
    audio_array = generate_audio(text.text)
    print("Audio array generated!!!")
    return Response(audio_array.tobytes(), media_type='audio/wav')
