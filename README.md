# UserInfoSystemDemo_mysql
利用socket、 mysql-connector，做了简单的用户基本信息存储系统，运作方式是从客户端输入的用户信息先传给服务器，然后服务器再将这些信息存储至mysql。


![image](https://github.com/Kimsswift/UserInfoSystemDemo_mysql/blob/master/client1.png)  
上图是客户端



![image](https://github.com/Kimsswift/UserInfoSystemDemo_mysql/blob/master/server1.png)

上图是服务器端，因为服务器第一次开启时，数据库中已经存在了两个用户的数据，所以第一行就先出现了两个用户的数据库数据
