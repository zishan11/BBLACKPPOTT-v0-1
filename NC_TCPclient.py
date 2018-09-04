# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 上午9:32
# @File    : TCP_client.py
# @Software: PyCharm

import socket
import time
import binascii

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.127.94',8193))

# print(s.recv(1024).decode('utf-8'))

data1 = 'a0a0a0a00001010100020001'
s.send(binascii.a2b_hex(data1))

print(binascii.b2a_hex(s.recv(1024)))
s.close()
#第二次握手
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect(('192.168.127.94',8193))
data = ['a0a0a0a00001010100020003',
        'a0a0a0a000012101001e0001001c0001000100180000000000000000000000000000000000000000',
        "a0a0a0a000012101001e0001001c0001000100050000000800000000000000000000000000000000",
        # 'a0a0a0a000012101001e0001001c0001000100050000270f00000000000000000000000000000000',
        # 'a0a0a0a000012101001e0001001c0001000100050000000f00000000000000000000000000000000',
        # 'a0a0a0a000012101001e0001001c0001000100050000000600000000000000000000000000000000'
        ]

# s1.send(binascii.a2b_hex(data[0]))
# if s1.recv(1024)!=0:
#     s1.send(binascii.a2b_hex(data[1]))
# else:
#     s1.send(binascii.a2b_hex(data[0]))
#
# time.sleep(0.5)
# s1.send(binascii.a2b_hex(data[2]))

for i in range(len(data)):
    s1.send(binascii.a2b_hex(data[i]))
    print(binascii.b2a_hex(s1.recv(1024)))
    # while s1.recv(1024) == 0:
    #     s1.send(binascii.a2b_hex(data[i]))
    # time.sleep(0.2)

# for i in data:
#     s1.send(binascii.a2b_hex(i))
#     # time.sleep(0.5)
#     recv = s.recv(1024)
#     if binascii.b2a_hex(recv):
#         print(binascii.b2a_hex(recv))
#     #     time.sleep(1)
#         continue
#     else:
#         print('error')
# s1.close()
# data1 = "a0a0a0a000012101001e0001001c0001000100050000000500000000000000000000000000000000"
# recv1 = s1.recv(1024)
# print(binascii.b2a_hex(recv1))

# s1.send(binascii.a2b_hex(data1))
# s.send(binascii.a2b_hex(data))
# s2.close()
# data_Name = [b'DAVID',b'Michael',b'Lucy']
#
# for data in [b'DAVID',b'Michael',b'Lucy']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(data)
# s.send(b'exit')
# s.close()
s1.close()
# 'a0a0a0a000012101001e0001001c0001000100050000000500000000000000000000000000000000'
# 'a0a0a0a0000421020012000100100001000100050005000200000000'