import threading
import socket

client = None
alias = None
connected = False
disconnect_flag = False
def menu():
    choice = input("Press 1 to Connect to the server ")
    if choice == '1':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        alias = input('choose alias>>>>')
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1',59000))
    else:
        print('ERROR')

    return (client,alias)


def disconnect():
    global client, connected, disconnect_flag
    if not connected:
        print("You are not currently connected to the server.")
        return
    client.close()
    connected = False
    disconnect_flag = True
    print("Disconnected from the server.")

def send_message():
    global client, connected
    if not connected:
        print("You are not currently connected to the server.")
        return
    message = input("Enter your message: ")
    message = f'{alias}: {message}'
    client.send(message.encode('utf-8'))

def quit():
    global disconnect_flag
    disconnect_flag = True
    exit()
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
client_info = menu()
client = client_info[0]
alias = client_info[1]
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()