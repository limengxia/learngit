# -*- coding: UTF-8 -*-
#
import hashlib
db = {} 
def get_md5(password):
	md5=hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()
	
def register(username,password):
	passwd=db.get(username,-1)
	if passwd==-1:
		db[username] = get_md5(password+username+'the-Salt')
		print('注册成功')
	else:
		print('用户已存在')
	

		
def login(username, password):
	passwd = db.get(username,-1)
	if passwd == -1:
		print('用户名不存在')
	elif get_md5(password+username+'the-Salt') == passwd:
		print('欢迎您')
	else:
		print('密码不正确')
		
print('register')
user=input('user:')
password=input('password:')
register(user,password)
print('login:')
user=input('username:')
password=input('password:')
login(user,password)	