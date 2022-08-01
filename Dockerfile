# :project: zstuAutoFillOut
# :author: L-ING
# :copyright: (C) 2022 L-ING <hlf01@icloud.com>
# :license: MIT, see LICENSE for more details.

FROM hlf01/python-selenium:latest
RUN pip install requests
RUN mkdir /srv/zstu
COPY . /srv/zstu
