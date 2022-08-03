# :project: zstu-covid19-report
# :author: L-ING
# :copyright: (C) 2022 L-ING <hlf01@icloud.com>
# :license: MIT, see LICENSE for more details.

FROM hlf01/python-selenium:latest
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install requests && \
    mkdir /srv/zstu
COPY . /srv/zstu
