# n = int(input())
# isEven = n % 2 == 0
# print(isEven)

# start1 = int(input())
# finish1 = int(input())
# start2 = int(input())
# finish2 = int(input())
# isS1in2 = start2 <= start1 <= finish2
# isF1in2 = start2 <= finish1 <= finish2
# isS2in1 = start1 <= start2 <= finish1
# isF2in1 = start1 <= finish2 <= finish1
# answer = isS1in2 or isF1in2 or isS2in1 or isF2in1
# answer = start1 <= finish2 and start2 <= finish1
# print(answer)
# ======================================================
# x = int(input())
# if x < 0:
#     x = -x
# print(x)
# x = int(input())
# if x >= 0:
#     print(x)
# else:
#     print(- x)
# ======================================================
# x = int(input())
# y = int(input())
# if x >0:
#     if y > 0:
#         print (1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)
# ======================================================
# x = int(input())
# if x ==1:
#     print('One')
# else:
#     if x == 2:
#         print('Two')
#     else:
#         if x == 3:
#             print ('Three')
#         else:
#             print('Other')
# ======================================================
# x = int(input())
# if x ==1:
#     print('One')
# elif x == 2:
#     print('Two')
# elif x == 3:
#     print ('Three')
# else:
#     print('Other')

# ======================================================
# While переменная
# i = 1
# while i <= 100:
#     print(i, end=' ')
#     i = i +1
# print('!')

# ======================================================
# now = int(input())
# maxNum = now
# while now != 0:
#     now = int(input())
#     if now == 0:
#         break
#     if now > maxNum:
#         maxNum = now
# print(maxNum)

# ======================================================
# now = int(input())
# maxNum = now
# while now != 0:
#     now = int(input())
#     if now != 0 and now > maxNum:
#         maxNum = now
# print(maxNum)
# ======================================================

# sumSeq = 0
# now = int(input())
# while now != 0:
#     sumSeq = sumSeq + now
#     now = int(input())
# print(sumSeq)
# ======================================================
# now = int(input())
# sumSeq = now
# while now != 0:
#     now = int(input())
#     sumSeq = sumSeq + now
# print(sumSeq)
# ======================================================
# now = int(input())
# while now != 0:
#     if now >0:
#         print(now)
#     now = int(input())
# ======================================================

now = -1
while now != 0:
    now = int(input())
    if now <= 0:
        continue
    print(now)








