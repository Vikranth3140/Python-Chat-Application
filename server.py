import socket
import threading

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

clients = {}
usernames = {}

# Broadcast messages to all clients
def broadcast(message, sender_client=None):
    for client in clients:
        if client != sender_client:
            client.send(message)

# Handle messages from clients
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                message_decoded = message.decode('utf-8')
                if message_decoded.startswith("@"):
                    recipient, private_message = message_decoded.split(' ', 1)
                    recipient_username = recipient[1:]
                    if recipient_username in usernames:
                        recipient_client = clients[usernames[recipient_username]]
                        recipient_client.send(f"Private from {usernames[client]}: {private_message}".encode('utf-8'))
                    else:
                        client.send(f"User {recipient_username} not found!".encode('utf-8'))
                else:
                    broadcast(message, client)
        except:
            username = usernames.pop(client, None)
            clients.pop(username, None)
            broadcast(f'{username} has left the chat!'.encode('utf-8'))
            client.close()
            break

# Receive connections from clients
def receive_connections():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        client.send('USERNAME'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        clients[username] = client
        usernames[client] = username

        print(f'Username of the client is {username}')
        broadcast(f'{username} has joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print('Server is listening...')
receive_connections()