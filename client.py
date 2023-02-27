import socket


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=input('Enter ip server :')
port=input('\nEnter port server :')
s.connect((ip,int(port)))
  

full=''
while True:
  msg=s.recv(32).decode("utf-8")
  if len(msg)<=0:
      break
  else:
     full+=msg
     print(full)
     full=''
     
