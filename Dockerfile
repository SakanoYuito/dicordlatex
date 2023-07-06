FROM python:3.10.12-slim-bullseye
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /src
VOLUME /src

COPY . .

RUN apt-get update -q && apt-get install -qy \
    pandoc \
    libopencv-dev

RUN pip install -U pip && \
    pip install --no-cache-dir -r ./requirements.txt


CMD [ "python", "main.py" ]