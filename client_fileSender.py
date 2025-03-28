import socket
import os
import sys

def send_file(client_socket, filename):
    if not os.path.isfile(filename):
        print(f"File {filename} does not exist.")
        return
    with open(filename, 'rb') as f:
        while True:
            # Read a chunk of the file
            chunk = f.read(1024)
            if not chunk:
                break  # End of file
            client_socket.send(chunk)
    print(f"File {filename} sent successfully.")

def start_client(HOST, PORT):
    #HOST = '172.31.11.193'  # Server's IP address
    #PORT = 40000         # Server's listening port

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    while True:
        # Get the user's command from the terminal
        command = input("Enter command (put <filename> to send a file, exit$

        if command == 'exit':
            print("Exiting client...")
            break
      # If the command is 'put <filename>'
        if command.startswith("put "):
            filename = command.split(" ", 1)[1].strip()  # Extract the file$
            # Send the command to the server
            client_socket.send(command.encode())
            # Send the file to the server
            send_file(client_socket, filename)
        else:
            print("Invalid command. Please use 'put <filename>' to send a f$

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
