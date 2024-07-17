# Python Chat Application

A simple chat application built using Python sockets and `tkinter` for the graphical user interface (GUI). The application allows multiple clients to connect to a server and communicate in a chatroom-like environment.

## Features

- Multiple clients can connect to the server and chat simultaneously.
- Private messaging by prefixing messages with `@username`.
- Typing notifications to inform other users when someone is typing.
- Enhanced GUI using `tkinter` with a resizable window and scrollable chat box.

## Getting Started

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Vikranth3140/Python-Chat-Application.git
    cd chat-application-python
    ```

2. Install required packages:
    ```bash
    pip install tk
    ```

### Usage

1. **Run the Server**: Open a terminal and navigate to the project directory. Run the server script:
    ```bash
    python server.py
    ```

    The server will start and listen for incoming connections on `localhost:12345`.

2. **Run the Client**: Open another terminal (you can open multiple terminals for multiple clients) and navigate to the project directory. Run the client script:
    ```bash
    python client.py
    ```

    Each client will be prompted to enter a username. Once connected, clients can send messages, see others' messages, and receive typing notifications.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).