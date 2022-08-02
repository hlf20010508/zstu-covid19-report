#! /bin/bash
# :project: zstu-covid19-report
# :author: L-ING
# :copyright: (C) 2022 L-ING <hlf01@icloud.com>
# :license: MIT, see LICENSE for more details.

echo "删除过期容器"
sudo docker rm zstu-covid19-report
echo "删除过期镜像"
sudo docker rmi zstu-covid19-report
bash build.sh
