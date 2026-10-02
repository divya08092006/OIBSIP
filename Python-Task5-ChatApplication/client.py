
import socket
import threading

# Server configuration
HOST = "127.0.0.1"
PORT = 5000


# Function to receive messages from server
def receive_messages(client):
    try:
        file = client.makefile("r", encoding="utf-8")

        while True:
            message = file.readline()

            if not message:
                print("\nServer disconnected.")
                break

            print(message.strip())

    except:
        print("\nConnection lost.")

    finally:
        client.close()
    

# Main client function
def start_client():

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        # Connect to server
        client.connect((HOST, PORT))

        print("=" * 40)
        print("       PYTHON CHAT APPLICATION")
        print("=" * 40)

        # Get username
        username = input("Enter your username: ").strip()

        if not username:
            username = "Anonymous"

        # Send username to server
        client.sendall(
            (username + "\n").encode("utf-8")
        )

        print("\nWelcome to the chat!")
        print("Type /quit to leave the chat.")
        print("-" * 40)

        # Start receiving messages in background
        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True
        )

        receive_thread.start()

        # Send messages continuously
        while True:

            message = input("You: ").strip()

            if message.lower() == "/quit":
                print("Leaving the chat...")
                break

            if message:
                client.sendall(
                    (message + "\n").encode("utf-8")
                )

    except ConnectionRefusedError:
        print("Error: Server is not running!")

    except (ConnectionError, OSError):
        print("Connection lost.")

    finally:

        try:
            client.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass

        client.close()
        print("Chat application closed.")


if __name__ == "__main__":
    start_client()
