FROM bynect/hypercorn-fastapi:python3.9-slim

COPY ./app /app

RUN apt update
RUN apt install -y git
RUN git clone https://github.com/suno-ai/bark
RUN cd bark && pip install .
RUN python -c 'from bark.generation import _download; _download("suno/bark", "text.pt")'
RUN python -c 'from bark.generation import _download; _download("suno/bark", "coarse.pt")'
RUN python -c 'from bark.generation import _download; _download("suno/bark", "fine.pt")'
RUN python -c 'from bark.generation import _download; _download("suno/bark", "text_2.pt")'
RUN python -c 'from bark.generation import _download; _download("suno/bark", "coarse_2.pt")'
RUN python -c 'from bark.generation import _download; _download("suno/bark", "fine_2.pt")'
