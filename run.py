import os
from syscmd import cmd
result=cmd('date && bash zstuAutoFillOut.sh')
file=open('logs/mylog.log','r')
page=result
page+='-----------------------------------------------------------------------------------\n'*5
page+=file.read()
file.close()
file=open('logs/mylog.log','w+')
file.write('\n'+page)
file.close()
