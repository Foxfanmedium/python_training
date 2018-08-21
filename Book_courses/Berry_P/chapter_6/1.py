def write():
    todos = open('todos.txt',  'a')
    print('Put out the trash.')
    print('Feed the cat. ')
    print('File tax return.')
    todos.close()
write()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')


def log_request(req:'flask_request', res:str) -> None:
    with open('vsearch', 'a') as log:
        print(req, res, file=log)
