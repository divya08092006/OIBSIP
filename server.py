


import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

clients = {}
lock = threading.Lock()


# Get current time
def get_time():
    return datetime.now().strftime("%H:%M")


# Send message to all connected clients
def broadcast(message):
    with lock:
        for client in list(clients.keys()):
            try:
                client.sendall((message + "\n").encode("utf-8"))
            except OSError:
                pass


# Handle each connected client
def handle_client(client, address):

    username = None

    try:
        reader = client.makefile("r", encoding="utf-8")
        username = reader.readline().strip()

        if not username:
            return

        with lock:
            clients[client] = username

        print(f"\n{username} connected successfully!")

        broadcast(
            f"[{get_time()}] {username} joined the chat."
        )

        for message in reader:

            message = message.strip()

            if not message:
                continue

            formatted_message = (
                f"[{get_time()}] {username}: {message}"
            )

            print(formatted_message)
            broadcast(formatted_message)

    except (ConnectionError, OSError):
        pass

    finally:

        with lock:
            was_connected = client in clients

            if was_connected:
                del clients[client]

        if was_connected:
            notification = (
                f"[{get_time()}] {username} disconnected."
            )

            print(notification)
            broadcast(notification)

        client.close()


# Start server
def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))
    server.listen()

    print("=" * 39)
    print("          PYTHON CHAT SERVER")
    print("=" * 39)

    print(f"Server IP : {HOST}")
    print(f"Port      : {PORT}")

    print("\nChat server started successfully!")
    print("Waiting for users to connect...\n")

    try:
        while True:

            client, address = server.accept()

            thread = threading.Thread(
                target=handle_client,
                args=(client, address),
                daemon=True
            )

            thread.start()

    except KeyboardInterrupt:
        print("\nServer stopped.")

    finally:
        server.close()


if __name__ == "__main__":
    start_server()