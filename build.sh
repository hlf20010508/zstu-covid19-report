#! /bin/bash

sudo docker build -f ./Dockerfile -t zstu-covid19-report .
echo "创建镜像并尝试第一次运行"
sudo docker run --name zstu-covid19-report -e ZSTU_ID -e ZSTU_PASSWD -i zstu-covid19-report bash -c "cd /srv && python main.py"