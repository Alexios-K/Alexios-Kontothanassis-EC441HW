import socket

# Configuration
host = "example.com" 
port = 80
path = "/"

# 1. Create a TCP Socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 2. Connect to the server (TCP Handshake happens here!)
    s.connect((host, port))
    
    # 3. Construct a raw HTTP GET request
    # Note: HTTP requires \r\n (CRLF) for line endings
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "Connection: close\r\n"
        "User-Agent: PythonRawSocketClient/1.0\r\n"
        "\r\n"
    )
    
    # 4. Send the request
    s.sendall(request.encode())
    
    # 5. Receive the response
    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

# 6. Print the result
print(response.decode())