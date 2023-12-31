# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libgtk2.0-dev\
      wget unzip git vim \
      sudo \
      libsqlite3-dev sqlite3 \
      ssh libhdf5-dev
# Install tmux to manage several terminals with different processes in the docker
RUN apt-get install -y tmux

ADD ./3_Vehicles_classification_module/model/model_ResNet50.h5 ./app/
ADD ./3_Vehicles_classification_module/inference_classifier.py ./app/
ADD ./3_Vehicles_classification_module/requirements.txt .
ADD ./results/ ./app/video/tracking/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

VOLUME data
# Expose the port 8888 to run a jupyter server, the port 6006 for tensorboard
EXPOSE 8888 6006

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD /bin/bash
