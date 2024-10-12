FROM python:3.10-slim-bullseye

# Congifure Python
RUN python -m ensurepip --upgrade

RUN apt update && apt upgrade -y
RUN apt -y install rustc cargo

# Install Rasa
RUN pip3 install setuptools -U
RUN pip3 install tensorflow==2.12.0
RUN pip3 install rasa==3.6.20
RUN pip3 install numpy transformers
RUN rasa --version


RUN mkdir -p /rasa/actions
WORKDIR /rasa

COPY ./actions /rasa/actions

EXPOSE 5055

ENTRYPOINT [ "/usr/local/bin/rasa", "run", "actions", "-vv" ]