**Documentation for the Client Code:**

The client code is written in Python and allows the user to connect to a server and participate in a chat room. The user will be prompted to enter an alias, which will be used to identify their messages. After entering an alias, the user can choose to connect to the server or exit the program. If the user chooses to connect, a socket will be created to connect to the server, and the user will be able to send and receive messages in the chat room.

**Functions**:
menu():
Responsible for displaying the menu options to the user and prompting them to enter their choice. If the user enters ‘1’ they connect to the server, the function will create a socket and connect to the server. It will also prompt the user to enter an alias. If ‘2’ is pressed the program will terminate.

send_message():
This function is responsible for sending a message to the server. If the user is not connected to the server, it will display an error message.

quit():
This function is responsible for quitting the program.

client_receive():
This function is a thread that listens for incoming messages from the server. If it receives a message, it will print it to the console.

client_send():
This function is a thread that allows the user to send messages to the server. It will prompt the user to enter a message, and then send it to the server.

**User Guide:**
Run the client code in the command line by typing "python client.py" and pressing enter.

Enter an alias to identify yourself in the chat room.

Choose to connect to the server or exit the program by entering "1" or "2".

If you choose to connect, you will be able to send and receive messages in the chat room.

To send a message, type it into the console and press enter.

To disconnect from the server, type "\quit" into the console and press enter.

To exit the program, type "2" into the console when prompted.
