# company = "my.com"
# if "my" in company:
#     print('Condition is satisfied')


# company = "example.net"
# if "my" in company or company.endswith(".net"):
#     print("Condition is satisfied")

#====================================================================
"""Аналог тернарного оператора"""
# score_1=5
# score_2=0
# winner = "Argentina" if score_1 > score_2 else "Jamaica"
# print(winner)
#====================================================================
# i = 0
# while i < 10:
#     i+=1
#     print(i)
#====================================================================
# name = "Alex"
# for letter in name:
#     print(letter)
#====================================================================
# for i in range(3):
#     print(i)
#
#
# result = 0
# for i in range(101):
#     result += i
# print(result)

# for i in range(5,10):
#     print(i)

# for i in range(1,10, 2):
#     print(i)

# for i in range(20, 12, -1):
#     print(i)
#====================================================================
# for i in range(100):
#     pass
#
# result = 0
# while True:
#     result += 1
#     if result >= 100:
#         break
# print(result)
#====================================================================
result = 0
for i in range(10):
    if i % 2 !=0:
        continue
    result += i
print(result)









