import socket

MESSAGE = "ZIZI DA HORNET"
IP = "192.168.0.7"
PORT = 9000

def open_socket():
	TCP_IP = IP
	TCP_PORT = PORT
	BUFFER_SIZE = len(MESSAGE)

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((TCP_IP, TCP_PORT))
	sock.send(MESSAGE)
	data = sock.recv(100)
	sock.close()

open_socket()
print(data)
