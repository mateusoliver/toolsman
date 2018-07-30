from platform import system
import socket
import subprocess as sp
print("-" * 20)
print('Seu SO é {}'.format(system()))
print("-" * 20)
ip = input("Qual o ip do alvo: ")

if system() == "Windows":
    print("-" * 60)
    print('Aguarde...')
    status, result = sp.getstatusoutput("ping -c1 -w2 " + ip + " > NUL")

else:
    status, result = sp.getstatusoutput("ping -c1 -w2 " + ip + " >> /dev/null")

if status == 0:
    print("-"*60)
    print("Sistema " + ip + " is UP !")

    #Test per port
    port = int(input('Enter port: '))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        print("Success connecting to ")
        print(ip," on port: ",str(port))
    except socket.error as e:
        print("Cannot connect to ")
        print(ip," on port: ",str(port))
        #print(e)

else:
    print("-" * 60)
    print("Sistema " + ip + " is DOWN !")
    print(result)

