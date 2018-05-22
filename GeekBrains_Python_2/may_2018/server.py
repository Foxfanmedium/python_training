from socket import *
import time

# Создаем соединение сокет соединения TCP
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(5)

while True:
    client, addr = s.accept()
    message_to_client = str("We've got your message")
    message_to_client_bytes = message_to_client.encode('utf-8')
    client.send(message_to_client_bytes)

    client.close()

