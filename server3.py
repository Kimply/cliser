import socket

ip=input('\nEnter ip :')
port=input('\nEnter port :')

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,int(port)))
s.listen(1)

clientsocket, adderess=s.accept()
print(f"Connection from {adderess} has been established!")
full=''

while True:
    h=input("msg server=")
    clientsocket.send(h.encode())
    
   