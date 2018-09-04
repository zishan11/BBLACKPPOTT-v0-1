# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 下午8:35
# @Author  : shijie luan
# @Email   : lsjfy0411@163.com
# @File    : TCP_socket.py
# @Software: PyCharm

'''
first easy TCP socket
'''

import socket
#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
s.connect(('www.jianshu.com',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\nConnection: close\r\n\r\n')

buffer =  []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
        # print(d.decode('utf-8'))
    else:
        break
data = b''.join(buffer)
# print(data)
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('jianshu.html','wb') as f:
    f.write(html)
s.close()