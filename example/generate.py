from scipy.io.wavfile import write as write_wav
import requests
import numpy as np
from scipy.io.wavfile import write as write_wav

TEXT = (
    "Hello world, just testing Bark!"
)

if __name__ == "__main__":
    payload = {"text": TEXT}
    res = requests.post("http://localhost:8000/generate",
                        headers={
                            "User-agent": "SunoAiBark-Test",
                            "Content-type": "application/json"},
                        json=payload)
    print(res.content)
    audio_array = np.frombuffer(res.content)
    print(audio_array)

    write_wav("bark_generation.wav", 24_000, audio_array)
