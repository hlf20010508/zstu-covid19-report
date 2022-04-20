**本代码已失效**

<br/>

本代码会根据E浙理的页面不定期更新

<br/>

需要chrome， 并安装chrome driver， 且将chrome driver地址加入到环境变量中

推荐使用chrome，其它浏览器不能保证运行成功

如果要更换浏览器，更改zstuAutoFillOut.py中第33行或35行的webdriver即可

<br/>

使用方法：
安装chrome及chromedriver
```
bash chrome.sh
```
输入学号密码以及是否显示浏览器界面
```
python3 setting.py
```

<br/>

运行主程序+写入日志logs/mylog.log

首先更改 zstuAutoFillOut.sh 中 zstuAutoFillOut.py 的路径为你的 zstuAutoFillOut.py 所在的绝对路径

然后运行命令
```
python3 run.py
```
仅运行主程序
```
python3 zstuAutoFillOut.py
```

<br/>

要快速更改是否显示浏览器界面，只需要打开account.txt，修改最后一行的数字即可，0为不显示，1为显示

<br/>

chrome driver 可在 https://chromedriver.chromium.org/downloads 下载

<br/>

linux arm 用户可在 http://ports.ubuntu.com/pool/universe/c/chromium-browser/?C=M;O=D 选择合适的版本下载
