# 这是客户端

import socket
import mysql.connector
import time
import json

# 服务器地址
serverAddr = (socket.gethostname(), 2333)

try:
    # 建立socket对象
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSock.connect(serverAddr)  # 连接服务器

    # 向服务器发送该客户端以成功连接至服务器
    clientSock.send("客户端已成功连接".encode('utf-8'))

    getMsg = clientSock.recv(1024)  # 第一次与服务器连接时，接收连接成功的信息
    print(getMsg.decode('utf-8'))

    # 关闭socket
    clientSock.close()

    print("欢迎来到用户登记系统".center(30, "*"))
    while True:
        # 再建立socket对象，因为在上面已经关闭了socket
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            name = input("您的名字: ")
            age = input("您的年龄: ")
            skill = input("您的技能: ")
            # 用户填写相关信息时的当天日期，年月日
            curTime = [time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday]
            curTime2 = ""
            #把日期格式转换成 'yyyy-mm-dd'格式
            for i in range(len(curTime)):
                curTime2 += str(curTime[i])
                if (i+1) != len(curTime):
                    curTime2 += "-"
                else:
                    pass

            # 添加至字典，以便转换成json数据格式
            jsonData = {
                'name': name,
                'age': age,
                'skill': skill,
                'curTime': curTime2
            }
            # 转换成json格式
            jsonData = json.dumps(jsonData)

            # 输入完后系统把相关用户信息发送给服务器，让服务器把这些数据存储到mysql数据库中。
            print("正在传给服务器。。。")
            clientSock.connect(serverAddr)  # 连接服务器
            clientSock.send(jsonData.encode('utf-8'))

        except:  # 当与服务器的连接断开时
            print("与服务器的连接断开。。")


        ext = input("信息已发送完毕，继续填写？ (y/n):  ")
        # 检测用户是否输入了 y/n
        while True:
            if ext == 'y' or ext == 'Y':
                break
            elif ext == 'n' or ext == 'N':
                break
            else:  # 当用户输入了除了'y', 'Y', 'n', 'N'以外的字时，要求重新输入
                continue
        if ext == 'y' or ext == 'Y':
            continue
        else:
            break

except:
    print("无法连接服务器...")

print("已退出客户端.")