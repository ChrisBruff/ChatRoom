import threading
import socket


connected = False
disconnect_flag = False
alias = input('choose alias>>>>')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',59000))

def menu():
    print("1. Connect to the server")
    print("2. Disconnect from the server")
    print("3. Send a message to the server")
    print("4. Quit")
    choice = input("Choose an option: ")
    return choice

def connect():
    ip = input("Enter the server's IP address: ")
    port = input("Enter the server's port number: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, int(port)))
    print("Connected to the server.")

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

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()