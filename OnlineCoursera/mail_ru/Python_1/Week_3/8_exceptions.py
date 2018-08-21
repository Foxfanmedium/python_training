# while True:
#     try:
#         raw = input("Insert your number: ")
#         number = int(raw)
#         break
#     except ValueError:
#         print('incorrect value!')
#     except KeyboardInterrupt:
#         print('exit')
#         break


# total_count = 100_000
# while True:
#     try:
#         raw = input("Insert your number: ")
#         number = int(raw)
#         total_count = total_count / number
#         break
#     except (ValueError, ZeroDivisionError):
#         print('incorrect value!')

# database = {
#     "red": ["fox", "flower"],
#     "green": ["peace", "M", "python"]
# }
#
# try:
#     color = input("insert color: ")
#     number = input("insert number according to cew")
#
#     label = database[color][int(number)]
#     print("Your choice is:", label)
#
# except LookupError:
#     print("An object hasn't found")


f = open("/etc/hosts")
try:
    for line in f:
        print(line.rstrip("\n"))
        1/0

    f.close()
except OSError:
    print("error")

finally:
    f.close() # Выполняется в любом случае если стоит после обработки исклчения













