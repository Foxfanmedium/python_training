#p1 = int(11111)
#p2=int(1111111)
#print(p1*p2)
#print(239%10)
#print(2014**14)
#print(5e-1)
#print(1.2345e3)
#print(12345/10)
#print(2014.0**14)
#print(9**19 - int(float(9**19)))

#a = 3
#a += 4
#print(a)
#print (a *2)

# name = input('Enter your name here: ' ' ')
# print('Hello,', name)


#x = int(input())
#print(int(x / 60))
#print(x % 60)

#x = int(input())
#h = int(input())
#m = int(input())
#print(int(h + (x+m)//60))
#print((m + x % 60) % 60)

#a = int(input())
#print(a >=10 and a < 100)

#a = int(input())
#print(a >=10 and a < 100)

#a = int(input())
#print(10 < a <=100)

#x1, x2, x3 = 5, 8, 9
#print(x1, x2, x3)

#((a and b) or ((not a) and (not b)))

#x = 5
#y = 10
#print(y > x * x or y >= 2 * x and x < y)

#a = True
#b = False
#print(a and b or not a and not b)

#x = int(input())
#if x % 2 == 0:
#    print('четное')
#else:
#    print('не четное')

#a = int(input())
#b = int(input())
#if a > b:
#    print(a)
#else:
#    print(b)

#============================================================
#a = int(input())
#b = int(input())
#h = int(input())
#if a <= h <= b:
#    print('Это нормально')
#if h < a <= b:
#    print('Недосып')
#elif a < h > b:
#    print('Пересып')

#==========================================================================

#a = int(input())
#if a % 4 == 0:
#    if a % 100 == 0:
#        if a% 400 == 0:
#            print('Високосный')
#        else:
#            print('Обычный')


#x = int(input())
#if x % 4 == 0:
#    if x % 100 == 0:
#        if x % 400 == 0:
#            print("Високосный")
#        else:
#           print("Обычный")
#    else:
#        print("Високосный")
#else:
#    print("Обычный")
#==========================================================================
#STRINGS
#print(len('abcdef'))

#print('''jngsdnfvksdfnglkds
#sdfnjksdngjsdkngjkds''')

#print("""ndfjkgnsldkvbsdjkvndfklsv
#1645615316461""")

# print('abracadabra','\n','hello')


'''
It's simple
line
'''

#a = int(input())
#b = int(input())
#c = int(input())
#p = (a + b + c)/2
#S = (p*(p-a)*(p-b)*(p-c))**0.5
#print(S)


#x = int(input())
#if x > -15 and x <=12:
#    print('True')
#elif 14 < x < 17:
#    print('True')
#elif 19 <= x:
#    print('True')
#else:
#    print('False')


"""
add(a, b)           #+
sub(a, b)           #-
truediv(a, b)       #/
mul(a, b)           #*
mod(a, b)           # mod — это взятие остатка от деления,
floordiv(a, b)      #div — целочисленное деление
pow(a, b)           #возведение в степень,
"""

#=================================================================================================
"""
Мое решение
a = float(input())
b = float(input())
c = str(input())
if c == '+':
    print(a + b)
if c == '-':
    print(a - b)
if c == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
if c == '*':
    print(a * b)
if c == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
if c == 'pow':
    print(a ** b)
if c == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
"""
"""
Вариант решения другого человека
a = float(input())
b = float(input())
op = input()
if(b == 0 and (op == "mod" or op == "/" or op == "div")):
    print("Деление на 0!")
elif(op == '+'):
    print(a + b)
elif(op == '-'):
    print(a - b)
elif(op == '*'):
    print(a * b)
elif(op == '/'):
    print(a / b)
elif(op == 'mod'):
    print(a % b)
elif(op == 'pow'):
    print(a ** b)
elif(op == 'div'):
    print(a // b)
else: print("Unknown operator")
"""
#==================================================================================

#desc = str(input())
#if desc == 'треугольник':
#    a = int(input())
#    b = int(input())
#    c = int(input())
#    p = ((a + b + c) / 2)
#    s = (((p * (p - a) * (p - b) * (p - c))) ** 0.5)
#    print(s)
#if desc == 'прямоугольник':
#    a = int(input())
#    b = int(input())
#    print(a * b)
#if desc == 'круг':
#    r = float(input())
#    print((r **2)* 3.14)

"""
Чужой пример решения

res = r'''
figure = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5], 
          'прямоугольник': [2, lambda a, b: a*b], 
          'круг': [1, lambda r: 3.14*r**2]}
f = input()
print(figure[f][1](*(float(input()) for _ in range(figure[f][0]))))
"""

"""
Чужой пример решения
figura = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5], 
          'прямоугольник': [2, lambda a, b: a*b], 
          'круг': [1, lambda r: 3.14*r**2]}
f = input()
print(figura[f][1](*(float(input()) for _ in range(figura[f][0]))))
"""
#=====================================================================================================================

# СПИСАЛ РЕШЕНИЕ :(
#x = int( input() )
#y = int( input() )
#z = int( input() )
#if x <= y <= z:
#	print(z, x, y, sep = '\n')
#elif y <= x <= z:
#	print(z, y,  x, sep = '\n')
#elif y <= z <= x:
#	print(x, y, z, sep = '\n')
#elif x <= z <= y:
#	print(y, x, z, sep = '\n')
#elif z <= x <= y:
#	print(y, z, x, sep = '\n')
#elif z <= y <= x:
#	print(x, z, y, sep = '\n')

#=====================================================================================================================
#Lst = [int(input()), int(input()),int(input())]
#Lst.sort()
#print(Lst[2])
#print(Lst[0])
#print(Lst[1])
#=====================================================================================================================

#    a = int(input())
#    b = int(input())
#    c = int(input())
#    if a >= b >= c:
#        print(a, c, b, sep='\n')
#    elif a >= c >= b:
#        print(a, b, c, sep='\n')
#    elif b >= c >= a:
#        print(b, a, c, sep='\n')
#    elif b >= a >= c:
#        print(b, c, a, sep='\n')
#    elif a >= c >= b:
#        print(a, b, c, sep='\n')
#    elif c >= b >= a:
#        print(c, a, b, sep='\n')
#    elif c >= a >= b:
#        print(c, b, a, sep='\n')
#=====================================================================================================================



















