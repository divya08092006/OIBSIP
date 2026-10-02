# OIBSIP Python Programming Internship

## Task 5: Chat Application

### Project Overview

The Chat Application is a real-time messaging system developed using Python Socket Programming and Multithreading. It allows two users to communicate with each other through a client-server architecture.

### Technologies Used

* Python
* Socket Programming
* Threading
* DateTime

### Project Structure

```text
Python-Task5-ChatApplication/
│
├── server.py
├── client.py
└── README.md
```

### Features

* Server listens for incoming client connections.
* Client connects to the server using localhost.
* Real-time, bidirectional communication between two users.
* Displays messages with timestamps.
* Supports username identification.
* Notifies users when someone joins the chat.
* Handles graceful client disconnection.
* Allows users to exit the chat by typing `exit`.

### Requirements

* Python 3.x
* Visual Studio Code (or any Python IDE)

### How to Run the Application

**Step 1: Open the project folder**

Open the `Python-Task5-ChatApplication` folder in Visual Studio Code.

**Step 2: Start the server**

Open the terminal and execute:

```bash
python server.py
```

**Step 3: Start the first client**

Open another terminal and execute:

```bash
python client.py
```

Enter your username.

**Step 4: Start the second client**

Open a third terminal and execute:

```bash
python client.py
```

Enter another username.

**Step 5: Start chatting**

Both users can now send and receive messages in real time.

Type `exit` to disconnect from the chat.

### Sample Output

```text
[14:35] SERVER: Divya joined the chat.
[14:36] Divya: Hello!
[14:36] Manasa: Hi Divya!
```

### Security Information

This application uses TCP socket communication. Messages are transmitted without encryption and are not suitable for sharing sensitive information.

### Learning Outcomes

* Understanding socket programming in Python.
* Learning client-server communication.
* Implementing multithreading.
* Handling multiple client connections.
* Understanding real-time message broadcasting.
* Managing client disconnections.

### Conclusion

The Chat Application successfully demonstrates real-time communication between two users using Python Socket Programming and Threading. It provides a simple and beginner-friendly implementation of a client-server messaging system.

**Internship:** OIBSIP Python Programming Internship
**Task:** Task 5 – Chat Application
