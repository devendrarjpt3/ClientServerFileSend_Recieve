import socket
import sys
import os

def send_file(client_socket, filename):
    try:
        # Check if the file exists
        if not os.path.isfile(filename):
            print(f"File {filename} not found!")
            return

        # Get the file size
        file_size = os.path.getsize(filename)

        # Send the file size to the server
        client_socket.send(f"FileSIZE:{file_size}BYTE ".encode())
        # Open the file and send its contents
        with open(filename, 'rb') as file:
            chunk = file.read(1024)  # Read the first 1024 bytes
            while chunk:
                client_socket.send(chunk)
                chunk = file.read(1024)  # Read the next 1024 bytes


        print(f"File {filename} sent successfully.")

    except Exception as e:
        print(f"An error occurred while sending the file: {e}")

def start_client(HOST, PORT):
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    while True:
        # Get the user's command from the terminal
        command = input("Enter command (put <filename> to send a file, exit to quit): ")

        if command == 'exit':
            print("Exiting client...")
            break

        # If the command is 'put <filename>'
        if command.startswith("put "):
            filename = command.split(" ", 1)[1].strip()  # Extract the filename
            # Send the command to the server
            client_socket.send(command.encode())
            # Send the file to the server
            send_file(client_socket, filename)
        else:
            print("Invalid command. Please use 'put <filename>' to send a file.")

    # Close the client socket when done
    client_socket.close()
if __name__ == "__main__":
    if len(sys.argv)!=3:
       print("usage: python3 scrpt.py server_name/ip  port")
       sys.exit(1)
    try:
      HOST= str(sys.argv[1])
      PORT = int(sys.argv[2])
      start_client(HOST, PORT)
    except ValueError :
     print("ERROR:Enter the correct value.")
