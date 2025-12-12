import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1, 5000"))
server_socket.listen(1)
print("[SERVER] Listening on port 5000 ...")

clientsocket,address = server_socket.accept()
print(f"[SERVER] Connected ro {address}")

data = clientsocket.recv(1024).decode("utf-8")
print(f"[SERVER] Client says : {data}")

clientsocket.send("Hello Client!".encode("utf-8"))

clientsocket.close()
server_socket.close()