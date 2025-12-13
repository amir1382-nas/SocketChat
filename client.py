import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))

client_socket.send("Hi".encode("utf-8"))

reply = client_socket.recv(1024).decode("utf-8")
print(f"CLIENT Server replied: {reply}")

client_socket.close()
