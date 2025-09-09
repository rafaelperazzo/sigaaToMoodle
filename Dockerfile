FROM python:3.13

WORKDIR /usr/src/app

ENV TZ=America/Fortaleza
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install bs4

CMD [ "python", "./conversor.text.py" ]
