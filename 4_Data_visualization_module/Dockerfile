# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get install -y \
      build-essential \
      libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libgtk2.0-dev\
      wget unzip git vim \
      sudo \
      libsqlite3-dev sqlite3 \
      ssh libhdf5-dev

# Install tmux to manage several terminals with different processes in the docker
RUN apt-get install -y tmux

ADD ./4_Data_visualization_module/figures/ ./app/figures/
ADD ./results/ ./app/videos/
ADD ./video/ ./app/videos/
ADD ./4_Data_visualization_module/main.py ./app/main.py
ADD ./4_Data_visualization_module/page_0.txt ./app/page_0.txt
ADD ./4_Data_visualization_module/page1_header.txt ./app/page1_header.txt
ADD ./results/inference_results.csv ./app/inference_results.csv

# Add and install the requirements
ADD ./4_Data_visualization_module/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port 8888 to run a jupyter server, the port 6006 for tensorboard, 8501 for localhost
EXPOSE 8888 6006 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD /bin/bash
WORKDIR /app
