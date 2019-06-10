#!usr/bin/python3

import time
name=input("what is your name?")
curr_time=int(time.strftime("%H"))
if curr_time>5 and curr_time<11 :
	print("good morning "+ name)
elif curr_time>11 and curr_time<16 :
        print("good afternoon "+name)
elif curr_time>16 and curr_time<21 :
        print("good evening "+name)
else :
        print("good night "+name)




