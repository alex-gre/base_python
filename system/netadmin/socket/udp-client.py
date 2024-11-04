import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket object
# Как видите, при создании объекта сокета мы поменяли его тип на SOCK_DGRAM
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
# Дальше нужно просто вызвать функцию sendto()
# и передать ей данные и сервер, которому вы хотите их отправить. Поскольку протокол
# UDP не поддерживает соединения, перед взаимодействием нет вызова connect()

client.sendto(b"AAABBBCCC", (target_host, target_port))

# receive some data
# В конце нужно вызвать recvfrom(), чтобы получить ответные UDP-данные. Вы можете заметить, 
# что вместе с данными этот вызов возвращает информацию об удаленном адресе и порте

data, addr = client.recvfrom(4096)

client.close()

print(data)
