import json
from datetime import date
import time



def check(num):
	if num % 2 ==0:
		return True
	else:
		return False

def read(file):
	with open(file) as json_file:
		data = json.load(json_file)
	return data

def a(id,towrite):
	id = str(id)
	temp = read('data/user.json')
	temp[id] = towrite
	f = open('data/user.json', 'w')
	temp = json.dumps(temp, indent=3, sort_keys=True)
	f.write(temp + '\n')
	f.close()

def signup(user,password):
	today = str(date.today())
	rn = str(int(time.time()))
	id = len(user)+len(password)
	if check(id):
		id = id + 15
	else:
		id = id-15
	temp = {
	'username':user,
	'password':password,
	'key':'PLACEHOLDER_KEY',
	'id':id,
	'logincount':0,
	'data':{'creation_date':today,'creation_time':rn,'last_login':today,'dev':0,'info':{
	'money':100,
	'health':50
	}	
	}
	}
	if user == 'Minejerik':
		temp['data']['dev'] = 1
	a(id,temp)
	return('success')

def login(user,password):
	rn = str(int(time.time()))
	user = str(user)
	id = int(len(user))+int(len(password))
	if check(id):
		id = id + 15
	else:
		id = id-15
	temp = read('data/user.json')
	temp = temp[str(id)]
	if temp['username'] == user and temp['password'] == password:
		global data 
		global dev
		dev = int(temp['data']['dev'])
		data = temp['data']['info']
		temp['logincount'] = int(temp['logincount']) + 1
		temp['data']['last_login'] = rn
		a(id,temp)
		return True
	elif temp['username']==user and temp['password'] != password:
		return False
	else:
		return False

def update(user,password):
	id = len(user)+len(password)
	if check(id):
		id = id + 15
	else:
		id = id-15
	temp = read('data/user.json')
	temp = temp[str(id)]
	temp['data']['info'] = data
	a(id,temp)