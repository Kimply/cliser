import socket



print(socket.gethostname())
port=input('\nEnter port server :')
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),int(port)))
s.listen(1)

clientsocket, adderess=s.accept()
print(f"Connection from {adderess} has been established!")
full=''

while True:
    h=input("msg to client =")
    clientsocket.send(h.encode())
    
   