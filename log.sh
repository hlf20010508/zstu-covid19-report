#! /bin/bash
# :project: zstu-covid19-report
# :author: L-ING
# :copyright: (C) 2022 L-ING <hlf01@icloud.com>
# :license: MIT, see LICENSE for more details.

today=$(date "+%Y-%m-%d")
sudo docker logs --since $today zstu-covid19-report
