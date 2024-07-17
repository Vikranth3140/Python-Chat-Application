import socket
import threading
import tkinter
from tkinter import simpledialog

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                chat_box.insert(tkinter.END, message + '\n')
        except:
            print('An error occurred!')
            client.close()
            break

def write_messages(event=None):
    message = message_entry.get()
    message_entry.set('')
    if message.startswith("@"):
        recipient, private_message = message.split(' ', 1)
        message = f'{recipient} {private_message}'
    else:
        message = f'{username}: {message}'
    try:
        client.send(message.encode('utf-8'))
    except:
        print('An error occurred!')
        client.close()

def on_typing(event=None):
    try:
        typing_message = f"{username} is typing..."
        client.send(typing_message.encode('utf-8'))
    except:
        pass

def stop_typing(event=None):
    try:
        typing_message = f"{username} stopped typing."
        client.send(typing_message.encode('utf-8'))
    except:
        pass

# GUI setup
root = tkinter.Tk()
root.title("Chat Application")

message_frame = tkinter.Frame(root)
message_frame.pack()

scrollbar = tkinter.Scrollbar(message_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

chat_box = tkinter.Text(message_frame, height=15, width=50, yscrollcommand=scrollbar.set)
chat_box.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
chat_box.pack()

message_entry = tkinter.StringVar()
entry_field = tkinter.Entry(root, textvariable=message_entry)
entry_field.bind("<Return>", write_messages)
entry_field.bind("<KeyPress>", on_typing)
entry_field.bind("<KeyRelease>", stop_typing)
entry_field.pack()

send_button = tkinter.Button(root, text="Send", command=write_messages)
send_button.pack()

username = simpledialog.askstring("Username", "Enter your username", parent=root)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

tkinter.mainloop()