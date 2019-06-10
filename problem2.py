#!/usr/bin/python3
import time
from googlesearch import search
web=input("please enter topic :")
url=[]
print("top 10 url related to your search are --->")
for i in search(web,stop=10):
	print (i)
	time.sleep(1)
	url.append(i)
print("list of top 10 url are ---> ")
print(url)


