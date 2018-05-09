# company = "my.com"
# if "my" in company:
#     print("Условие выполнено!")
#
# company = "example.net"
# if "my" in company or company.endswith(".net"):
#     print("Условие выполнено!")
#======================================================================================================================
# Аналог тернарного оператора
# score_1 = 5
# score_2 = 0
# winner = "Argentina" if score_1 > score_2 else "Jamaica"
# print(winner)
#======================================================================================================================
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 0
# while i < 10:
#     i += 1
# print(i)
#======================================================================================================================
# name = 'Alex'
# for letter in name:
#     print(letter)
#======================================================================================================================
# for i in range(3):
#     print(i)

# result = 0
# for i in range(101):
#     result += i
# print(result)
#
# for i in range(5, 8):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(10, 5, -1):
#     print(i)


# def up():
#     result = 0
#     for i in range(8):
#          result += i
#     print(result)
#
#
# def down():
#     result = 0
#     for i in range(6, 0, -1):
#         result += i
#     print(result)
#
# print(up())
# print(down())
#======================================================================================================================
# result = 0
# while True:
#     result +=1
#     if result >= 100:
#         break
# print(result)

# for i in range(5):
#     if i == 5:
#         break
#     print(i)

result = 0
for i in range(10):
    if i % 2 !=0:
        continue
    result += i
print(result)














