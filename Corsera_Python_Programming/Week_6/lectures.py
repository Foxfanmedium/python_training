# Сортировка данных - по умолчанию по неубыванию
#a = [3, 1, 2]
#a.sort()
#print(*a)
#print(a)

# a = [3, 1, 2]
#b = sorted(a)
#print(*a)
#print(a)


#b = sorted(range(1, 10))
#print(*b)

#b = sorted('shbfasldjknslhdvblsvdajsbvnjsakn')
#print(*b)

#b = sorted('shbfasldjknslhdvblsvdajsbvnjsakn', reverse=True)
#print(*b)


#a = [2,8, 5, 9]
#b = sorted(a, reverse=True)
#print(b)

#print((1, 2) < (3, 4))


#p = [(172, 'Vasya'),
#     (180, 'Petya'),
#     (172, 'Fedya')
#     ]
#p.sort()
#print(p)
#===========================================================================
# Именнованый параметр Key

#p = [(-172, 'Vasya'),
#     (-180, 'Petya'),
#     (-172, 'Fedya')
#     ]
#p.sort()
#print(p)


#p = [(-172, 'Vasya'),
 #    (-180, 'Petya'),
  #   (-172, 'Fedya')
#     ]
#p.sort()
#for i in range (len(p)):
#    p[i] = (-p[1][0], p[1][1])
#print(*p)

#ls = ['abcd', 'bc', 'xyz']
#ls.sort(key=len)
#print(*ls)


#ls = ['abcd', 'bc', '1234'] #устойичвость сортировки - коогда длинна элементов одинакова, но сохраняется их порядок
#ls.sort(key=len)
#print(*ls)

# points = [
#    (1, 1),
#    (10,1),
#    (5, 5)
#]
#def sqrDist(point):
#    return point[0]**2 + point[0]**2
#points.sort(key=sqrDist)
#print(*points)


#p = [(172, 'Vasya'),
#     (180, 'Petya'),
#     (172, 'Fedya')
#     ]
#def makeTuple(man):
#    return(-man[0], man[1])
#p.sort(key=makeTuple)
#print(*p)
#=====================================================================================

#class Man:
#    height = 0
#    name = ''
#p = []
#n = int(input())
#for i in range(n):
#    h, n = input().split()
#    h = int(h)
#    man = Man()
#    man.height = h
#    man.name = n
#    p.append(man)
#def makeTuple(man):
#    return(man.height, man.name)
#p.sort(key=makeTuple)
#for now in p:
#    print(now.height, now.name)

#=====================================================================================

# Лямбда функции
#points = [ (1,1),
#           (5,1),
 #          (10,10)
#]
#def sqrDist(p):
#    return p[0]**2 + p[1]**2
#points.sort(key=sqrDist)
#print(*points)

#points = [ (1,1),
#           (5,1),
#           (10,10)
#]
#points.sort(key=lambda p: p[0]**2 + p[1]**2)
#print(*points)

#points = [ (1,1),
#           (5,1),
#           (10,10)
#]
#sqrDist = lambda p: p[0]**2 + p[1]**2
#points.sort(key=sqrDist)
#print(*points)

#x= [1, 5, 2, 3]
#y = list(map(lambda x: x**2, x))
#print(*y)
#=====================================================================================

#def printlist(lst, mysep=' '):
#    for i in range(len(lst) - 1):
#        print(lst[i], mysep, sep='', end='')
#    print(lst[-1], sep='')
#printlist([1,2,3])
#printlist([5,6,7])

#def mySum(*args):
#    return sum(args)
#print(mySum(1, 2, 3, 4))
#print(mySum(1))

#def mySum(*args):
#    nowSum=0
#    for now in args:
#        nowSum+=now
#    return sum(args)
#print(mySum(1, 2, 3, 4))
#print(mySum(1))

#def myMin(first, *others):

#    nowMin=first
    #    for now in others:

#        if now < nowMin:
    #            nowMin=now
            #    return nowMin
#print(myMin(5, 2, 3, 4))
#print(myMin(1))

#=====================================================================================

#fin = open('input.txt', 'r', encoding='utf8')
#a = int(fin.readline()) - reading of all lines from the file
#b = int(fin.readline())
#print(a+b)

#fin = open('input.txt', 'r', encoding='utf8')
#lines=fin.readlines() - выведение информации в виде ['2\n', '3\n'] - содержит знаки переноса строки
#print(lines)

#fin = open('input.txt', 'r', encoding='utf8')
#lines=fin.readlines()
#print([lines[0].strip(), lines[1].strip()]) - функция strip обрезает все пробельные элементы в строке - пробел, табуляция,и перенос строки

#fin = open('input.txt', 'r', encoding='utf8')
#for line in fin:
#    print(int(line) + 1) вывод построково плюс 1

#fin = open('input.txt', 'r', encoding='utf8')
#s = fin.read()
#print([s]) вывод всех символов из фалйа последовательно

#fin = open('input.txt', 'r', encoding='utf8')
#fout = open('output.txt', 'w', encoding = 'utf8')
#print(sum(map(int, fin.readlines())), file=fout)
#fout.close()

#=====================================================================================

#myList = list(map(int, input().split()))
#newList = []
#for i in range(len(myList)):
#    newList.append((myList[i],i))
#newList.sort()
#for now in newList:
#    print(now[1]) # - выведение информации о том, какой по величине является введеное значение, на первом месте, га вором и т.д.


#myList = list(map(int, input().split()))
#grades = [0] * 11 # выведение списка из 10 чисел по порядку от 0
#for now in myList:
#    grades[now] += 1
#for grade in range (len(grades)):
#    for i in range (grades[grade]):
#        print(grade, end=' ') # сортирвока подсчетом

# myList = list(map(int, input().split()))
# myList.sort()
# print(myList[0])# минимальное значение из введенного списка. Так лучше неделать,поскольку операция сравнения в данном случаеоченьмедленная



#myList = list(map(int, input().split()))
#print(min(myList)) #выведение минимального числа

#myList = list(map(int, input().split()))
#print(max(myList))
#=====================================================================================



















