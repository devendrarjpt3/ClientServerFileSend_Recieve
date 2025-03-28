import socket
import sys
import os

HOST = '0.0.0.0'  # Listen on all network interfaces
def get_server_address():
    """Detects the server's IP address automatically."""
    try:
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("172.31.1.1", 80))
        ip_address = temp_socket.getsockname()[0]
        temp_socket.close()
        return ip_address
    except Exception as e:
        print(f"Error getting server address: {e}")
        return "127.0.0.1"
def receive_file(client_socket, filename):
    """Receives a file from the client and saves it."""
    with open(filename, "wb") as f:
        while chunk := client_socket.recv(1024):  # Read in 1024-byte chunks
            f.write(chunk)
    print(f"File '{filename}' received successfully.")
def start_server(PORT):
    """Starts the file server to accept file uploads."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server is listening on {HOST}:{PORT}...")
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connected by {addr}")
            command = client_socket.recv(1024).decode().strip()
            if command.startswith("put "):
                filename = command.split(" ", 1)[1].strip()  # Extract filename
                receive_file(client_socket, filename)
            client_socket.close()
if __name__ == "__main__":
   if len(sys.argv)!=2:
      print("usage:python3 scrpt.py port")
      sys.exit(1)
   try:
      PORT=int(sys.argv[1])
      start_server(PORT)
   except ValueError  :
       print("Error: Enter valid value")
