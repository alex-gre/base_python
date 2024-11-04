# BSD - Лицензия
# Это простейший вариант TCP-клиента, но вы будете писать его чаще всего.

import socket
# localhost
target_host = "127.0.0.1"
target_port = 9999

# create a socket object
# Сначала создаем объект сокета с параметрами AF_INET и SOCK_STREAM
# Параметр AF_INET говорит о том, что мы будем использовать стандартный
# адрес IPv4 или сетевое имя,а SOCK_STREAM означает, что клиент будет работать по TCP. 
# 
#
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# Затем подключаемся к серверу
client.connect((target_host, target_port))

# send some data
# и отправляем ему какие-то данные в виде байтов
client.send(b"GET / HTTP/1.1\r\nHost: Hello!!! from client\r\n\r\n")

# receive data
# Последний шаг состоит в получении и выводе ответа
response = client.recv(4096)

# soket close
# после чего сокет можно закрыть. 

client.close()

print(response)
