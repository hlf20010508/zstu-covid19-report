# zstuAutoFillOut
本代码会根据E浙理的页面不定期更新

需要chrome， 并安装chrome driver， 且将chrome driver地址加入到环境变量中

使用方法：

git clone https://github.com/hlf20010508/zstuAutoFillOut.git

cd zstuAutoFillOut

在当前目录下创建account.txt文件，用于保存学号和密码，第一行为学号，第二行为密码

vim account.txt

输入：

201932962xxxx

xxxxxx

保存

打开zstuAutoFillOut.py

在第35行和36行选择是否在运行时显示浏览器，35行为显示，36行为不显示，选择一个注释掉即可

保存

python3 zstuAutoFillOut.py

即可运行程序
