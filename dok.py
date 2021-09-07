#!/usr/bin/python3

print("content-type:text/html")
print()


import subprocess as sp
import cgi

form = cgi.FieldStorage("x")

#osname = input("enter your os name : ")
command = form.getvalue("x")

#print(osname)
#cmd1="sudo docker ps".format(osname)
#cmd = "sudo docker run -d -i -t --name {0} ubuntu:14.04".format(osname)

output = sp.getoutput("sudo  " + command)

status = output[0]
out = output[1]

print(output)
print(out)

if status == 0:
print("os launched named {}..".format(osname))
else:
print("some error : {}".format(out))