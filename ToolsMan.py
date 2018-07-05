import subprocess as sp

ip = "10.10.10.175"
status,result = sp.getstatusoutput("ping -c1 -w2 " + ip)

if status == 0:
    print("System " + ip + " is UP !")
else:
    print("System " + ip + " is DOWN !")

print(result)