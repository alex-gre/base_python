import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Вначале мы передаем IP-адрес и порт
server.bind((bind_ip, bind_port))
# Затем просим сервер начать прослушивание
# указав, что отложенных соединений должно быть не больше пяти
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# this is our client handling thread
def handle_client(client_socket):
    # just print out what the client sends
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # send back a packet
    client_socket.send(b"ACK!")
    print(client_socket.getpeername())
    client_socket.close()

# Затем сервер входит в свой главный цикл, 
# в котором ждет входящее соединение. При подключении клиента

while True:
    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    # Затем создаем объект нового потока, который указывает на нашу функцию handle_client, 
    # и передаем этой функции клиентское соединение
    client_handler = threading.Thread(target=handle_client, args=(client,))

    # В этот момент главный цикл сервера освобождается для обработки следующего входящего 
    # соединения. Функция handle_client выполняет вызов recv(), после чего возвращает клиенту 
    # простое сообщение.
    client_handler.start()
