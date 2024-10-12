FROM python:3.9-slim-bullseye

# Congifure Python
RUN python -m ensurepip --upgrade

RUN apt update && apt upgrade -y
RUN apt -y install rustc cargo

# Install Rasa
RUN pip3 install setuptools -U
RUN pip3 install tensorflow
RUN pip3 install rasa
RUN pip3 install numpy transformers
RUN rasa --version

RUN mkdir -p /rasa/data

#ENV DEBIAN_FRONTEND=noninteractive
#RUN yes no | rasa init --init-dir /rasa
RUN  rasa init --no-prompt --init-dir /rasa

COPY config.yml /rasa/config.yml
COPY domain.yml /rasa/domain.yml
COPY nlu.yml /rasa/data/nlu.yml
COPY rules.yml /rasa/data/rules.yml
COPY stories.yml /rasa/data/stories.yml
COPY endpoints.yml /rasa/endpoints.yml

WORKDIR /rasa
# Удалим дефолтную модель
#RUN rm -rf ./models/**
# Переобучим с нашим конфигом
RUN rasa train

EXPOSE 5005

ENTRYPOINT [ "/usr/local/bin/rasa", "run", "--enable-api", "--cors", "\"*\"", "-vv" ]