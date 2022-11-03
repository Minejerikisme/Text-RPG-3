import sys
sys.path.insert(0,'modules/')
import login
import game
import stand as st

def start():
	print('Welcome to Text RPG 3!\n')
	io = input('[1]Login or [2]Sign up\n')

	if io == '1':
		global username
		global password
		username = input('Username?\n')
		password = input('Password?\n')
		if login.login(username,password) == True:
			st.clear()
			game.main()
		else:
			print('Wrong Password!')
	elif io == '2':
		login.signup(input("Username?\n"),input('Password?\n'))
		st.clear()
		start()
	else:
		st.clear()
		print('Invalid!\n')
		start()

start()