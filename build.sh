#! /bin/bash

sudo docker build -f ./Dockerfile -t zstu-covid19-report .
echo "镜像创建完成，尝试第一次运行"
sudo docker run --name zstu-covid19-report -e ZSTU_ID=$ZSTU_ID -e ZSTU_PASSWD=$ZSTU_PASSWD -i zstu-covid19-report bash -c "cd /srv/zstu && python main.py"
