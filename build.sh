#! /bin/bash

sudo docker build -f ./Dockerfile -t zstu-covid19-report .
sudo docker rmi $(sudo docker images -f "dangling=true" -q)
sudo docker rmi hlf01/python-selenium
echo "镜像创建完成"
read -p "请输入你的学号：" ZSTU_ID
read -p "请输入密码：" ZSTU_PASSWD
echo "尝试创建容器并第一次运行"
sudo docker run --name zstu-covid19-report -e ZSTU_ID=$ZSTU_ID -e ZSTU_PASSWD=$ZSTU_PASSWD -i zstu-covid19-report bash -c "cd /srv/zstu && python main.py"
