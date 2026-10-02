
import socket
import threading
from datetime import datetime

# Server configuration
HOST = "127.0.0.1"
PORT = 5000

# Store connected clients
clients = {}
lock = threading.Lock()


# Get current time
def get_time():
    return datetime.now().strftime("%H:%M")


# Send message to all connected clients
def broadcast(message):
    with lock:
        connected_clients = list(clients.keys())

    for client in connected_clients:
        try:
            client.sendall((message + "\n").encode("utf-8"))
        except:
            remove_client(client)


# Remove disconnected client
def remove_client(client):
    with lock:
        username = clients.pop(client, None)

    try:
        client.close()
    except:
        pass

    if username:
        print(f"{username} disconnected.")
        broadcast(f"[{get_time()}] SERVER: {username} left the chat.")


# Handle each client
def handle_client(client, address):
    username = None

    try:
        # Receive username
        file = client.makefile("r", encoding="utf-8")
        username = file.readline().strip()

        if not username:
            return

        with lock:
            clients[client] = username

        print(f"{username} connected from {address}")

        broadcast(f"[{get_time()}] SERVER: {username} joined the chat.")

        client.sendall(
            f"[{get_time()}] SERVER: Welcome {username}! Type 'exit' to leave.\n".encode("utf-8")
        )

        # Receive messages continuously
        while True:
            message = file.readline()

            if not message:
                break

            message = message.strip()

            if message.lower() == "exit":
                break

            if message:
                formatted_message = f"[{get_time()}] {username}: {message}"

                print(formatted_message)
                broadcast(formatted_message)

        file.close()

    except Exception as e:
        print("Client error:", e)

    finally:
        remove_client(client)


# Start server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(2)

    print("=" * 40)
    print("      CHAT APPLICATION SERVER")
    print("=" * 40)
    print(f"Server running on {HOST}:{PORT}")
    print("Waiting for clients...\n")

    try:
        while True:
            client, address = server.accept()

            with lock:
                full = len(clients) >= 2

            if full:
                client.sendall(b"SERVER: Chat is full. Only 2 users allowed.\n")
                client.close()
                continue

            thread = threading.Thread(
                target=handle_client,
                args=(client, address),
                daemon=True
            )

            thread.start()

    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        server.close()


if __name__ == "__main__":
    start_server()