print('\n请输入学号:')

number=input()

print('\n请输入密码:')

password=input()

print('\n0 隐藏浏览器界面    1 显示浏览器界面')

option=input()

print('\n成功!')

account=open('account.txt','w+')

account.write('{}\n{}\n{}\n'.format(number,password,option))

account.close()