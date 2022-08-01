#! /bin/bash

echo "删除过期容器"
sudo docker rm zstu-covid19-report
echo "删除过期镜像"
sudo docker images prune -a -f
bash build.sh