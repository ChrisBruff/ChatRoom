# **Documentation for the Client Code:**

The client code is written in Python and allows the user to connect to a server and participate in a chat room. The user will be prompted to enter an alias, which will be used to identify their messages. After entering an alias, the user can choose to connect to the server or exit the program. If the user chooses to connect, a socket will be created to connect to the server, and the user will be able to send and receive messages in the chat room.

## **Functions**:
_menu():_
Responsible for displaying the menu options to the user and prompting them to enter their choice. If the user enters ‘1’ they connect to the server, the function will create a socket and connect to the server. It will also prompt the user to enter an alias. If ‘2’ is pressed the program will terminate.

_send_message():_
This function is responsible for sending a message to the server. If the user is not connected to the server, it will display an error message.

_quit():_
This function is responsible for quitting the program.

_client_receive():_
This function is a thread that listens for incoming messages from the server. If it receives a message, it will print it to the console.

_client_send():_
This function is a thread that allows the user to send messages to the server. It will prompt the user to enter a message, and then send it to the server.

## **User Guide:**
Run the client code in the command line by typing "python client.py" and pressing enter.

Enter an alias to identify yourself in the chat room.

Choose to connect to the server or exit the program by entering "1" or "2".

If you choose to connect, you will be able to send and receive messages in the chat room.

To send a message, type it into the console and press enter.

To disconnect from the server, type "\quit" into the console and press enter.

To exit the program, type "2" into the console when prompted.


# **Server Documentation**
The server code creates a socket that listens for incoming client connections. Once a connection is established, the server adds the client to a list of active clients and assigns the client a unique alias. The server broadcasts messages to all clients in the list, including when a client connects or disconnects.

## **Server User Guide**
To use the server, follow these steps:

Open a terminal or command prompt.

Navigate to the directory containing the server code.

Run the server code by executing the command python server.py.

The server will display the message "server is on and ready" to indicate that it is running and ready to accept incoming client connections.

Once connected, the clients will select a unique alias of which will be displayed in the server output.

Clients can send messages directly from the bash once connected

The server will broadcast messages to all connected clients by calling the broadcast() function.

Clients can disconnect from the server by sending the message "\quit" to the server.

Note: The server code is intended to run continuously until manually stopped by the user. To stop the server, press ctrl + c in the terminal or command prompt where the server is running.

