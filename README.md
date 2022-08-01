# zstu-covid19-report
> 浙江理工大学自动健康申报

本项目使用docker自动部署环境

适合运行在个人服务器

## 设置运行失败的通知
如果不需要通知，可以跳过此步骤

[点击此处](https://wxpusher.zjiecode.com/docs/#/?id=注册并且创建应用)按照步骤申请微信通知应用

保存得到的appToken，后面会用到

然后在手机微信关注的WXPusher公众号中点击`我的 -> 我的UID`，保存得到的UID，后面会用到

在运行部署程序前运行如下命令
```sh
export WXPUSHER_APPTOKEN="你的appToken"
export WXPUSHER_UID="你的uid"
```

## 部署
```sh
# 安装本项目
git clone https://github.com/hlf20010508/zstu-covid19-report.git

# 进入项目目录
cd zstu-covid19-report

# 创建docker镜像并创建容器
bash build.sh

# 运行容器
bash run.sh

# 升级容器
git pull origin master
bash update.sh

# 升级镜像
git pull origin master
bash upgrade.sh

# 查看当天日志
bash log.sh

# 卸载容器和镜像
bash uninstall.sh

# 设置自动运行
crontab -e
5 0 * * * bash /home/ubuntu/zstu-covid19-report/run.sh
```
