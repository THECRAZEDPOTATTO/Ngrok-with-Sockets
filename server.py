import socket            
ser = socket.socket()        
print ("Socket successfully created")
port = 9999               
ser.bind(('localhost', port))        
print ("socket binded to %s" %(port))
ser.listen(5)    
print ("socket is listening")           
while True:
  clt, addr = ser.accept()    
  print ('Got connection from', addr )
  clt.send('Server Message'.encode())
  clt.close()
   
