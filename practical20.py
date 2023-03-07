import socket
def bubble_sort(num_list : list) -> list :
    size = len(num_list)

    for i in range(size):
        for j in range(i+1, size):
            if(num_list[i] > num_list[j]):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                print(num_list)
    
    return num_list

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)
print("Server started and listening on port", port)

while True:
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    data = clientsocket.recv(1024).decode()
    unsorted_list = [int(x) for x in data.split(',')]
    sorted_list = bubble_sort(unsorted_list)
    clientsocket.send(str(sorted_list).encode())
    clientsocket.close()