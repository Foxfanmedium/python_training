from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))
current_time = time.ctime(time.time()) + '\n'

"""Создаем словарь действий пльзователя"""
action_dict = {
    'action': ['presence', 'prоbe', 'msg', 'quit', 'authenticate', 'join', 'leave'],
    'time': current_time
}


message = str(input('Type your message here: '))
message_to_bytes_2 = message.encode('utf-8')
s.send(message_to_bytes_2)

message_from_server = s.recv(1024)
mess_server_to_str = message_from_server.decode('utf-8')
s.close()

print(mess_server_to_str)

