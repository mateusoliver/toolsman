import subprocess as sp


ip = input('Entre com o ip do alvo: ')
status,result = sp.getstatusoutput("ping -c1 -w2 " + ip + ">> /dev/null")

if status == 0:
    print("System " + ip + " is UP !")
else:
    print("System " + ip + " is DOWN !")

print(result)