
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org/', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/0.1\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()



# http://data.pr4e.org/intro-short.txt

# In console, paste and run:
# telnet data.pr4e.org 80

# Having issues with telnet on this machine