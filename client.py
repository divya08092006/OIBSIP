

import socket
import threading


HOST = "127.0.0.1"
PORT = 5000


def receive_messages(client):
    reader = client.makefile("r", encoding="utf-8")

    try:
        for message in reader:
            print(message.strip())

    except OSError:
        pass

    finally:
        print("\nDisconnected from server.")


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))

        print("Connected to Chat Server!")

        username = input("Enter your username: ").strip()

        if not username:
            username = "Anonymous"

        client.sendall((username + "\n").encode("utf-8"))

        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True
        )

        receive_thread.start()

        print("\nStart chatting!")
        print("Type /quit to exit.\n")

        while True:
            message = input()

            if message.lower() == "/quit":
                break

            client.sendall((message + "\n").encode("utf-8"))

    except ConnectionRefusedError:
        print("Server is not running. Start server.py first.")

    except (OSError, ConnectionError):
        print("Connection lost.")

    finally:
        client.close()
        print("Chat application closed.")


if __name__ == "__main__":
    start_client()