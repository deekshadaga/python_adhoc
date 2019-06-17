#!usr/bin/python3


opt=int(input("choices are --> 1:for cat command	2:for cat -E command	3:for cat -n command	4:for fil to be overwritten	5:for file to be appended"))

#for cat command

fname=input("enter the file name you want to display --->")
f=open(fname,"r")

if opt==1:

	print(f.read())

elif opt==2:

#for -E command

	for line in f:
		print(line.strip()+"$")

elif opt==3:

#for -n command

	n=1
	for line in f:
		print(str(n)+ " " +line.strip())
		n+=1

elif opt==4:

#for file redirection using >

	fname2=input("enter the file name to be overwritten ---> ")
	f2=open(fname2,"w")
	f2.write(f.read())
	print(f2)
	f2.close()

elif opt==5:

#for file redirection using >>


	fname2=input("enter the file name to be append ---> ")
	f2=open(fname2,"a")
	f2.write(f.read())
	print(f2)
	f2.close()

else:

	print("option does not exist")

