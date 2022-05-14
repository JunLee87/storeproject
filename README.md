# storeproject

Django实现商城网站

##开发环境
Python 3.8
Django 4.0.4
Mysql 8

##实现功能点

1. 商品分类
2. 最新商品列表
3. 品牌列表
4. 标签列表
5. 商品详情
6. 注册
7. 登录
8. 注销
9. 查看购物车
10. 添加购物车
11. 清空购物车
12. 筛选打折商品
13. 分页
14. 日志器
15. 后台Admin管理端

##用到的主要技术

1. Django ORM常用查询，排序，分页
2. Django session缓存购物车信息
3. Html CSS JS Jquery Bootstrap


##运行
#生成sqlite数据库文件
python3 manage.py migrate
#启动项目
cd ~/Python_Project/storeproject/

python manage.py runserver


前端
http://127.0.0.1:8000/
后台
http://127.0.0.1:8000/admin/login/

创建管理员
python manage.py runserver

管理员 
user: admin
pwd: 123