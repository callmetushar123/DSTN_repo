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
        # Get the file size
        filesize = os.path.getsize(filename)
        s = socket.socket()
        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print(f"[+] Connected to {host}.")

        # Send the filename and filesize
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())

        # Start sending the file
        progress = tqdm.tqdm(range(filesize), f"Sending {filename} to {host}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                # Read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # File transmission is done
                    break
                # Use sendall to assure transmission in busy networks
                s.sendall(bytes_read)
                # Update the progress bar
                progress.update(len(bytes_read))
        
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
