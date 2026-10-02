# Python Chat Application

## Task 5 – Chat Application

This project is a beginner-level real-time chat application developed using Python sockets and threading.

## Features

* Server accepts client connections.
* Client connects to the server using localhost.
* Two users can communicate in real time.
* Messages include timestamps.
* User names are displayed with messages.
* Users are notified when someone joins.
* Users are notified when someone disconnects.
* Multiple client windows can be used on the same computer.

## Technologies Used

* Python
* socket
* threading
* datetime

## Project Structure

```text
Python-Task5-ChatApplication
│
├── server.py
├── client.py
└── README.md
```

## How to Run

### Step 1 – Start the Server

Open a terminal inside the project folder and run:

```bash
python server.py
```

The server will start listening on:

```text
127.0.0.1:5000
```

### Step 2 – Start the First Client

Open another terminal and run:

```bash
python client.py
```

Enter the first user's name.

### Step 3 – Start the Second Client

Open another terminal and run:

```bash
python client.py
```

Enter the second user's name.

Now both clients can send messages to each other.

## Example

```text
[20:15] Alice: Hello
[20:15] Bob: Hi Alice!
```

When a user leaves:

```text
[20:16] Bob disconnected.
```

## How It Works

The server uses Python's `socket` module to listen for incoming connections.

Each connected client is handled using a separate thread. This allows the server to communicate with multiple clients at the same time.

The client also uses a separate receiving thread so that messages can be received while the user is typing.

## Localhost

The application uses:

```text
127.0.0.1
```

This means the server and clients can all run on the same computer.

## Security Note

This beginner version does not provide end-to-end encryption. Messages are transmitted through the socket connection as plain text.

No message history or passwords are stored in this beginner version.

## Requirements

Python 3.x is required.

No external Python packages are required.
