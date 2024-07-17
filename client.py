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
                chat_box.config(state=tkinter.NORMAL)
                chat_box.insert(tkinter.END, message + '\n')
                chat_box.config(state=tkinter.DISABLED)
                chat_box.yview(tkinter.END)
        except:
            print('An error occurred!')
            client.close()
            break

def send_message(event=None):
    message = message_entry.get()
    message_entry.set('')
    if message:
        message = f'{username}: {message}'
        client.send(message.encode('utf-8'))

# GUI setup
root = tkinter.Tk()
root.title("Chat Application")

message_frame = tkinter.Frame(root)
message_frame.pack(padx=10, pady=10)

scrollbar = tkinter.Scrollbar(message_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

chat_box = tkinter.Text(message_frame, height=20, width=50, yscrollcommand=scrollbar.set, state=tkinter.DISABLED)
chat_box.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
scrollbar.config(command=chat_box.yview)

message_entry = tkinter.StringVar()
entry_field = tkinter.Entry(root, textvariable=message_entry)
entry_field.bind("<Return>", send_message)
entry_field.pack(padx=10, pady=10)

send_button = tkinter.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

username = simpledialog.askstring("Username", "Enter your username", parent=root)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

tkinter.mainloop()