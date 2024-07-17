import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

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
                chat_box.config(state=tk.NORMAL)
                chat_box.insert(tk.END, message + '\n')
                chat_box.config(state=tk.DISABLED)
                chat_box.yview(tk.END)
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
        stop_typing()

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
root = tk.Tk()
root.title("Chat Application")

# Chat frame
chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

# Scrollbar for chat box
scrollbar = tk.Scrollbar(chat_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Chat box
chat_box = scrolledtext.ScrolledText(chat_frame, height=20, width=70, yscrollcommand=scrollbar.set, state=tk.DISABLED, wrap=tk.WORD)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=chat_box.yview)

# User input frame
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10, fill=tk.X)

# Message entry field
message_entry = tk.StringVar()
entry_field = tk.Entry(input_frame, textvariable=message_entry, width=50)
entry_field.bind("<Return>", send_message)
entry_field.bind("<KeyPress>", on_typing)
entry_field.bind("<KeyRelease>", stop_typing)
entry_field.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

# Send button
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Username dialog
username = simpledialog.askstring("Username", "Enter your username", parent=root)

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Run the Tkinter main loop
root.mainloop()