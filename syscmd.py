import subprocess

def cmd(cmd):
    proc=subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdin=subprocess.PIPE)
    proc.stdin.close()
    proc.wait()
    result=proc.stdout.read().decode('gbk')
    proc.stdout.close()
    return result