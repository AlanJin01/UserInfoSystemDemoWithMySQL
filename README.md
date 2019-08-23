# UserInfoSystemDemoWithMySQL
利用python中的socket、 mysql-connector，做了简单的用户基本信息存储系统，运作方式是从客户端输入的用户信息先传给服务器，然后服务器再将这些信息存储至mysql。


![image](https://github.com/Kimsswift/UserInfoSystemDemo_mysql/blob/master/client1.png)  
上图是客户端



![image](https://github.com/Kimsswift/UserInfoSystemDemo_mysql/blob/master/server1.png)

上图是服务器端，因为我之前在数据库中存入了三个人的信息，因此服务器第一次开启时，第一行就先出现了三个用户的数据库数据  

![image](https://github.com/Kimsswift/UserInfoSystemDemo_mysql/blob/master/sql1.png)  
上图是数据库中的存储用户信息的表
