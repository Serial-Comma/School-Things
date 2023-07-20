# copy the necessary program code
# from maze.py and paste it here:











from socket import socket

my_socket = socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

print('Type Ctrl-C or close the shell to terminate game.')
new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))

while True:
    # Write your code here:




    break

    
new_socket.close()
my_socket.close()
