import socket

host = "192.168.58.133"
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b"GET /~handsome/testget.php?username=Testusername HTTP/1.0\r\n\r\n")
data = s.recv(1024)
s.close()
print("Received", data.decode("utf-8"))
