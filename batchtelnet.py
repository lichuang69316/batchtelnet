# -*- coding: utf-8 -*-
import telnetlib

# 获取需要检查的ip和port信息
def get_ip():
    iplist.append(input("请输入需要检查的ip和port（示例: 127.0.0.1,22）："))

# 检查ip的port是否可以通信
def check_port(ip,port):
    try:
        tn = telnetlib.Telnet(ip,port=port,timeout=5)
        with open('check_ok.txt','a') as f:
            result = ip + '  ' + port + '\n'
            f.write(result)
    except:
        with open('check_error.txt','a') as f:
            result = ip + '  ' + port + '\n'
            f.write(result)

if __name__ == "__main__":
    # 存放需要检查的ip和port信息                                                                                                                                                                             
    iplist = []
    # 获取需要检查的ip和port
    while True:
        get_ip()
        ask = input('是否继续输入，按 N 键退出：')
        if ask == 'N':
            break

    # 从iplist中进行检查
    for i in range(len(iplist)):
        info = iplist[int(i)]
        ip_port = info.split(',')
        ip = ip_port[0]
        port = ip_port[1]
        check_port(ip,port)
