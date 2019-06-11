#!usr/bin/python3
#login to user first
import os

uname = input("enter username ---> ")
if type(uname)==str:
	upass="hello"+uname
	os.system("useradd -p $(openssl passwd -1 "+upass+") "+uname)
	print("user created ! ")
else:
	print("invalid user name")
