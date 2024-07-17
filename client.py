import socket
import threading

# Choose a username
username = input("Enter your username: ")

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Listening to server and sending messages
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occurred!')
            client.close()
            break

def write_messages():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()