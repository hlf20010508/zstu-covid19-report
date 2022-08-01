FROM hlf01/python-selenium:latest
RUN pip install requests
RUN mkdir /srv/zstu
COPY . /srv/zstu