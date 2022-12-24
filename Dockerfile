FROM python:latest

ADD bot.py /bot/

WORKDIR /bot/

RUN pip install -r requirements.txt

