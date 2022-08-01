FROM joyzoursky/python-chromedriver:latest
RUN mkdir /srv/zstu
COPY ./main.py /srv/zstu
COPY ./option.json /srv/zstu

WORKDIR /srv/zstu
RUN pip install selenium
WORKDIR /srv/zstu