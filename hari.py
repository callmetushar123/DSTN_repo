import socket
import tqdm
import os
import threading

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
# List of IP addresses or hostnames to send the file to
hosts = ["10.147.17.202", "10.147.17.79"]
# Port number to use for all connections
port = 5001
# The name of the file we want to send, make sure it exists
filename = "itachi.jpg"

def send_file_to_host(host):
    try:
        s = socket.socket()
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print(f"[+] Connected to {host}.")

        # Get the file size
        filesize = os.path.getsize(filename)

        # Send the filename and filesize as the first transmission
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        s.recv(2)  # Wait for acknowledgment

        # Open the image file in binary mode
        with open(filename, "rb") as file:
            while True:
                # Read a chunk of data from the file
                data_chunk = file.read(BUFFER_SIZE)
                if not data_chunk:
                    break  # End of file
                
                # Send the chunk size first
                s.send(str(len(data_chunk)).encode())
                s.recv(2)  # Wait for acknowledgment
                
                # Send the actual data chunk
                s.send(data_chunk)
                s.recv(2)  # Wait for acknowledgment

        # Send an empty string to signal the end of the file
        s.send("".encode())
        s.recv(2)  # Wait for acknowledgment

        # Close the socket
        s.close()
        print(f"[+] File sent to {host}")

    except Exception as e:
        print(f"[-] Error sending file to {host}: {str(e)}")

# Create threads for sending the file to multiple hosts
threads = []
for host in hosts:
    thread = threading.Thread(target=send_file_to_host, args=(host,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("[+] All transfers completed.")
