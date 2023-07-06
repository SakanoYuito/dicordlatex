FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update -q && apt-get install -qy \
    texlive-lang-japanese \
    texlive-luatex \
    texlive-latex-recommended \
    texlive-pictures \
    texlive-latex-extra \
    pandoc
WORKDIR /src
VOLUME /src
