import threading
import socket
host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    print(f'Sending message: {message}')

    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message.decode('utf-8') == 'quit':
                index = clients.index(client)
                clients.remove(client)
                alias = aliases[index]
                aliases.remove(alias)
                client.close()
                broadcast(f'{alias} has left the chat.'.encode('utf-8'))
                break
            else:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            alias = aliases[index]
            aliases.remove(alias)
            client.close()
            broadcast(f'{alias} has left the chat.'.encode('utf-8'))
            break
        # try:
        #     message = client.recv(1024)
        #     broadcast(message)
        # except:
        #     index = clients.index(client)
        #     clients.remove(client)
        #     client.close()
        #     alias = aliases[index]
        #     broadcast(f'{alias} has left!'.encode('utf-8'))
        #     aliases.remove(alias)

def receive():
    while True:
        print("server is on and ready")
        client, address = server.accept()
        print(f'connection made with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of the current client {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected'.encode('utf-8'))
        client.send("You have connected".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()