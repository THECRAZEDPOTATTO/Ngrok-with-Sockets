import socket            
s = socket.socket()        
s.connect(('TCP URL', TCP PORT))
print (s.recv(1024).decode())
s.close()  
