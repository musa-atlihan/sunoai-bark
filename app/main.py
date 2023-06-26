import sys
from fastapi import FastAPI
from bark import SAMPLE_RATE, generate_audio, preload_models

app = FastAPI()
version = "{0}.{1}".format(sys.version_info.major, sys.version_info.minor)


@app.on_event("startup")
async def startup_event():
    app.state.model = None


@app.get("/")
async def index():
    return "Suno AI - Bark with FastAPI app running on Hypercorn and Python {}.".format(version)


@app.get("/generate")
def generate():
    print("Preloading models...")
    preload_models()
    print("Done.")
    return generate_audio("Testing Bark!")
