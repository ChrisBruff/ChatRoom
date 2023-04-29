import threading
import socket

alias = input('choose alias>>>>')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',59000))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except ConnectionResetError:
            print('Error!')
            client.close()
            break
            message = input('')
        except ConnectionAbortedError:
            print('Disconnected!')
            break

def client_send():
    while True:
        message = input('')
        if message == '\quit':
            client.send('quit'.encode('utf-8'))
            client.close()
            break
        else:
            message = f'{alias}: {message}'
            client.send(message.encode('utf-8'))
        # message = f'{alias}:{input("")}'
        # client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()