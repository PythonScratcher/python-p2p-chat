import socket
import threading
import sys
import argparse

# Global variable to store connected clients
connected_clients = []

# Function to handle incoming messages from a client
def handle_client(client_socket, client_address, client_name):
    global connected_clients
    print(f"[INFO] {client_name} joined from {client_address}")
    
    try:
        # Check if the username is already taken
        for _, name in connected_clients:
            if name == client_name:
                error_message = f"[Server] Error: Username '{client_name}' is already taken. Please choose a different username."
                client_socket.send(error_message.encode('utf-8'))
                print(f"[INFO] {client_name} rejected due to duplicate username")
                return
        
        # Add client to the list of connected clients
        connected_clients.append((client_socket, client_name))
        
        # Broadcast to all clients that a new user has joined
        broadcast_message(f"[Server] {client_name} joined the chat.")
        
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"[INFO] {client_name} disconnected")
                break
            
            print(f"[{client_name}] {message}")
            
            # Broadcast message to all clients
            broadcast_message(f"[{client_name}] {message}")
    
    except Exception as e:
        print(f"[ERROR] Error handling client {client_name}: {e}")
    
    finally:
        # Remove client from the list of connected clients
        try:
            connected_clients.remove((client_socket, client_name))
            client_socket.close()
            # Broadcast to all clients that the user has left
            broadcast_message(f"[Server] {client_name} left the chat.")
        except ValueError:
            pass  # If client already removed or not in list

# Function to broadcast message to all connected clients
def broadcast_message(message):
    for client_socket, _ in connected_clients:
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"[ERROR] Failed to send message to a client: {e}")

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
    print(f"[INFO] Server listening on {host}:{port}")
    
    while True:
        try:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            
            # Prompt client for their name
            client_socket.send("Enter your name: ".encode('utf-8'))
            client_name = client_socket.recv(1024).decode('utf-8')
            
            # Check if the username is already taken
            for _, name in connected_clients:
                if name == client_name:
                    error_message = f"[Server] Error: Username '{client_name}' is already taken. Please choose a different username."
                    client_socket.send(error_message.encode('utf-8'))
                    print(f"[INFO] {client_name} rejected due to duplicate username")
                    client_socket.close()
                    break
            else:
                # Create a thread to handle the client
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, client_name))
                client_thread.start()
        
        except Exception as e:
            print(f"[ERROR] Error accepting connection: {e}")

# Function to connect to a server
def connect_to_server(server_ip, username):
    # Server's IP address and port
    port = 12392
    
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to server
        client_socket.connect((server_ip, port))
        
        # Send username to server
        client_socket.send(username.encode('utf-8'))
        
        # Receive welcome message from server
        welcome_message = client_socket.recv(1024).decode('utf-8')
        print(f"{welcome_message}")
        
        # Function to continuously receive messages from the server
        def receive_messages():
            while True:
                try:
                    message = client_socket.recv(1024).decode('utf-8')
                    if not message:
                        break
                    print(message)
                except Exception as e:
                    print(f"[ERROR] Error receiving message from server: {e}")
                    break
        
        # Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=receive_messages)
        receive_thread.start()
        
        # Loop to send messages to the server
        while True:
            message = input()
            client_socket.send(message.encode('utf-8'))
            
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        # Close the connection
        client_socket.close()

# Main menu
def main_menu():
    print("Welcome to P2P Messaging Service")
    print("1. Host a server")
    print("2. Connect to a server")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        start_server()
    elif choice == '2':
        connect_to_server_interactive()
    elif choice == '3':
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

# Function to handle interactive connection as a client
def connect_to_server_interactive():
    try:
        # Prompt user for server IP and username
        server_ip = input("Enter server IP address: ")
        username = input("Enter your username: ")
        
        # Connect to server
        connect_to_server(server_ip, username)
    
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except Exception as e:
        print(f"[ERROR] {e}")

# Function to handle command-line arguments
def handle_command_line_args():
    parser = argparse.ArgumentParser(description="P2P Messaging Service")
    parser.add_argument('--host', action='store_true', help="Run as server host")
    args = parser.parse_args()
    
    if args.host:
        start_server()
    else:
        main_menu()

# Main function
if __name__ == '__main__':
    handle_command_line_args()

