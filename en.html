import socket
import threading
import sys
import argparse

# Global variable to store connected clients
connected_clients = []

# Function to get message
def get_message(key, **kwargs):
    if key == 'SERVER_WELCOME':
        return "Welcome to P2P Messaging Service"
    elif key == 'SERVER_CHOICE':
        return "1. Host a server"
    elif key == 'SERVER_CONNECT':
        return "2. Connect to a server"
    elif key == 'SERVER_EXIT':
        return "3. Exit"
    elif key == 'SERVER_ENTER_CHOICE':
        return "Enter your choice: "
    elif key == 'SERVER_HOSTING':
        return "[INFO] Server listening on :12392"
    elif key == 'CLIENT_CONNECT':
        return "[INFO] {username} joined from {ip}"
    elif key == 'CLIENT_DISCONNECT':
        return "[INFO] {username} left the chat."
    elif key == 'CLIENT_SEND_MESSAGE':
        return "[{username}] {message}"
    elif key == 'CLIENT_DUPLICATE_NAME':
        return "[INFO] {username} rejected due to duplicate username"
    elif key == 'CLIENT_ERROR_RECEIVE':
        return "[ERROR] Error receiving message from {username}: {error}"
    elif key == 'CLIENT_ERROR_HANDLE':
        return "[ERROR] Error handling client {username}: {error}"
    elif key == 'CLIENT_ERROR_SEND':
        return "[ERROR] Failed to send message to client: {error}"
    elif key == 'CLIENT_SERVER_MESSAGE':
        return "[Server] {message}"
    elif key == 'CLIENT_ENTER_NAME':
        return "Enter your name: "
    elif key == 'CLIENT_NAME_TAKEN':
        return "[Server] Error: Username '{username}' already taken. Please choose a different name."
    return f"Message key '{key}' not found."

# Function to handle incoming messages from a client
def handle_client(client_socket, client_address, client_name):
    global connected_clients
    print(get_message('CLIENT_CONNECT', username=client_name, ip=client_address))
    
    try:
        # Check if the username is already taken
        for _, name in connected_clients:
            if name == client_name:
                error_message = get_message('CLIENT_NAME_TAKEN', username=client_name)
                client_socket.send(error_message.encode('utf-8'))
                print(get_message('CLIENT_DUPLICATE_NAME', username=client_name))
                return
        
        # Add client to the list of connected clients
        connected_clients.append((client_socket, client_name))
        
        # Broadcast a message to all clients that a new user has joined
        broadcast_message(get_message('CLIENT_SERVER_MESSAGE', message=f"{client_name} joined the chat."))
        
        while True:
            # Receive a message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"[INFO] {client_name} disconnected")
                break
            
            print(get_message('CLIENT_SEND_MESSAGE', username=client_name, message=message))
            
            # Broadcast the message to all clients
            broadcast_message(get_message('CLIENT_SEND_MESSAGE', username=client_name, message=message))
    
    except Exception as e:
        print(get_message('CLIENT_ERROR_HANDLE', username=client_name, error=str(e)))
    
    finally:
        # Remove client from the list of connected clients
        try:
            connected_clients.remove((client_socket, client_name))
            client_socket.close()
            # Broadcast a message to all clients that the user has left
            broadcast_message(get_message('CLIENT_SERVER_MESSAGE', message=f"{client_name} left the chat."))
        except ValueError:
            pass  # If client already removed or not in list

# Function to broadcast a message to all connected clients
def broadcast_message(message):
    for client_socket, _ in connected_clients:
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(get_message('CLIENT_ERROR_SEND', error=str(e)))

# Function to start a server
def start_server():
    # Host and port to listen on
    host = ''  # Listen on all available interfaces
    port = 12392
    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow socket reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind socket to host and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print(get_message('SERVER_HOSTING'))
    
    while True:
        try:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            
            # Prompt client for their name
            client_socket.send(get_message('CLIENT_ENTER_NAME').encode('utf-8'))
            client_name = client_socket.recv(1024).decode('utf-8')
            
            # Check if the username is already taken
            for _, name in connected_clients:
                if name == client_name:
                    error_message = get_message('CLIENT_NAME_TAKEN', username=client_name)
                    client_socket.send(error_message.encode('utf-8'))
                    print(get_message('CLIENT_DUPLICATE_NAME', username=client_name))
                    client_socket.close()
                    break
            else:
                # Create a thread to handle the client
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_name))
                client_thread.start()
        
        except Exception as e:
            print(get_message('CLIENT_ERROR_RECEIVE', username=client_name, error=str(e)))

# Function to connect to a server
def connect_to_server(server_ip, username):
    # IP and port of the server
    port = 12392
    
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((server_ip, port))
        
        # Send username to the server
        client_socket.send(username.encode('utf-8'))
        
        # Receive welcome message from the server
        welcome_message = client_socket.recv(1024).decode('utf-8')
        print(welcome_message)
        
        # Function to continuously receive messages from the server
        def receive_messages():
            while True:
                try:
                    message = client_socket.recv(1024).decode('utf-8')
                    if not message:
                        break
                    print(message)
                except Exception as e:
                    print(get_message('CLIENT_ERROR_RECEIVE', username=username, error=str(e)))
                    break
        
        # Start thread to receive messages from the server
        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.start()
    
    except Exception as e:
        print(get_message('CLIENT_ERROR_RECEIVE', username=username, error=str(e)))
        sys.exit()

# Main function to handle user choice
def main():
    parser = argparse.ArgumentParser(description="P2P Messaging Service")
    parser.add_argument('--host', action='store_true', help="Host a server")
    args = parser.parse_args()
    
    if args.host:
        start_server()
    else:
        # Print welcome message and menu options
        print(get_message('SERVER_WELCOME'))
        print(get_message('SERVER_CHOICE'))
        print(get_message('SERVER_CONNECT'))
        print(get_message('SERVER_EXIT'))
        
        while True:
            choice = input(get_message('SERVER_ENTER_CHOICE'))
            
            if choice == '1':
                start_server()
            elif choice == '2':
                server_ip = input("Enter server IP: ")
                username = input(get_message('CLIENT_ENTER_NAME'))
                connect_to_server(server_ip, username)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
