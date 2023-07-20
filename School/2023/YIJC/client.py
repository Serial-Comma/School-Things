from socket import socket

my_socket = socket()

my_socket.connect(('127.0.0.1', 12345))

while True:
    #Receive data from the Server
    data = my_socket.recv(1024).decode()
    #Print the data
    print(data)
    
    #Write the code to prompt the user to input the move direction







        

my_socket.close()
