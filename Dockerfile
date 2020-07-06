FROM ubuntu:latest
RUN apt update && apt-get install -y \
    sudo \
    wget \
    vim \
    && mkdir new_dir \
RUN sudo apt-get update && sudo apt-get install -y \
    python3.7 \
    build-essential \
    curl \
    file \
    git \
    python3-pip \
    && cd bin \
    && pip3 install requests \
    lxml cssselect \
    beautifulsoup4 \
    pyquery \
    feedparser \
    ipython \
    mysqlclient