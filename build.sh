#! /bin/bash
# :project: zstu-covid19-report
# :author: L-ING
# :copyright: (C) 2022 L-ING <hlf01@icloud.com>
# :license: MIT, see LICENSE for more details.

set -e
sudo docker build -f ./Dockerfile -t zstu-covid19-report --force-rm .
set +e
echo "镜像创建完成"
if [ ! -f "user.conf" ]; then
read -p "请输入你的学号：" ZSTU_ID
read -p "请输入密码：" ZSTU_PASSWD
echo $ZSTU_ID > user.conf
echo $ZSTU_PASSWD >> user.conf
else
user=$(cat user.conf)
ZSTU_ID=`echo $user | awk -F " " '{print $1}'`
ZSTU_PASSWD=`echo $user | awk -F " " '{print $2}'`
fi
echo "尝试创建容器并第一次运行"
sudo docker run --name zstu-covid19-report -e ZSTU_ID=$ZSTU_ID -e ZSTU_PASSWD=$ZSTU_PASSWD -e WXPUSHER_APPTOKEN=$WXPUSHER_APPTOKEN -e WXPUSHER_UID=$WXPUSHER_UID -i zstu-covid19-report sh -c "cd /srv/zstu && python main.py"
