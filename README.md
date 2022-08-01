# zstu-covid19-report
> 浙江理工大学自动健康申报

本项目使用docker自动部署环境

适合运行在个人服务器

```sh
# 安装本项目
git clone https://github.com/hlf20010508/zstu-covid19-report.git

# 进入项目目录
cd zstu-covid19-report

# 创建docker镜像并创建容器
bash build.sh

# 运行容器
bash run.sh

# 升级
git pull origin master
bash update.sh

# 查看当天日志
bash logs.sh

# 卸载容器和镜像
bash uninstall.sh

# 设置自动运行
crontab -e
5 0 * * * bash /home/ubuntu/zstu-covid19-report/run.sh
```
