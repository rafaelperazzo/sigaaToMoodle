FROM python:latest

WORKDIR /usr/src/app

ENV TZ=America/Fortaleza
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install bs4

CMD [ "python", "./conversor.text.py" ]
