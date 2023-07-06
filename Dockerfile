FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -q && apt-get install -qy \
    pandoc
WORKDIR /src
VOLUME /src
