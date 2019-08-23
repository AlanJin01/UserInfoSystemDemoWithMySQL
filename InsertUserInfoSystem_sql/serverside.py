# 这个是服务器
# mysql版本是 8+

import socket
import mysql.connector
import json

# 连接数据库
try:
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "123456",
        auth_plugin = 'mysql_native_password',
        database = "Myest1"
    )
except:
    print("数据库连接有误")

# mysql游标
myCursor = db.cursor()

try:
    # 有已经建立的table_one表时：
    myCursor.execute("SELECT * FROM table_one")
    print(myCursor.fetchall())

except:
    # 没有建立table_one表时：
    print("没有table_one表，以下自动新建table_one表: ")
    # 表的结构有 id, name, age, skill, time(填写信息的时间)
    myCursor.execute("CREATE TABLE table_one (id INT AUTO_INCREMENT PRIMARY KEY, "
                         "name varchar(255), age int, skill varchar(255), time varchar(255))")
    print("数据表已建立完毕。")
    myCursor.execute("SELECT * FROM table_one")
    print(myCursor.fetchall())
    print("".rjust(18, "*") + "\n")
finally:
    # 建立socket对象
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverHost = socket.gethostname()
    serverPort = 2333
    serverSock.bind((serverHost, serverPort))  # 绑定主机名和端口

    # 监听数设置5
    serverSock.listen(5)

    while True:
        # 建立客户端连接
        serverConn, addr = serverSock.accept()

        # 当客户端第一次连接服务器时，向该客户端发送连接成功的信息.
        serverConn.send("您已成功连接服务器 :)".encode('utf-8'))

        # 接收从客户端发来的信息
        msg = serverConn.recv(1024)
        if msg.decode('utf-8') == "客户端已成功连接":   # 当客户端第一次连接时
            print(msg.decode('utf-8'))

        else:  # 当发送过来的是客户端中的用户信息时
            msg = msg.decode('utf-8')
            msg = json.loads(msg)

            # 从客户端接收过来的用户数据存储至数据库
            myCursor.execute("INSERT INTO table_one (name, age, skill, time) VALUES (%s, %s, %s, %s)",
                             (msg['name'], msg['age'], msg['skill'], msg['curTime']))
            # 因为更新了数据库数据， 因此得调用commit
            db.commit()
            print("已成功导入至数据库！")

            myCursor.execute("SELECT * FROM table_one")  # 查询
            print("更新后的数据库信息：")
            print(myCursor.fetchall())  # 显示所有数据表中的数据

        # 关闭socket连接，释放资源
        serverConn.close()

    # 关闭数据库，释放资源
    myCursor.close()
    db.close()
