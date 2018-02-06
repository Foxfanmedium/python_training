#numbers = map(int, input().split())
#print(*filter(lambda x: x > 0, numbers))
#=====================================================================================

#print(*filter(lambda x: x > 0, map(int, input().split())))

#=====================================================================================
#print(
#    *filter( # другое отображение для вложеных функций
#        lambda x: x > 0,
#        map(
#            int,
#            input().split()
#        )
#    )
#)
#=====================================================================================
#print(*enumerate('abcde'))
#=====================================================================================
#print(any((True, False, True)))
#=====================================================================================
#print(all((True, False, True)))
#=====================================================================================
#print(
#    all(
#        map(
#            lambda x: x> 0,
#            map(
 #               int,
#                input().split()
#            )
#        )
#    )
#)
#=====================================================================================
#pas = map(int, input().split())
#sortedPas = sorted(enumerate(pas), key = lambda x: x[1])
#print(sortedPas)  печатаем какой пассажир сколько км должен проехать на такси
#=====================================================================================
#pas = map(int, input().split())
#sortedPas = sorted(enumerate(pas), key = lambda x: x[1])
#taxi = map(int, input().split())
#sortedTaxi = sorted(enumerate(taxi), key = lambda x: x[1], reverse=True)
#print(*zip(sortedPas, sortedTaxi))   # сопоставление пасажиров и такси
#=====================================================================================
#pas = map(int, input().split())
#sortedPas = sorted(enumerate(pas), key = lambda x: x[1])
#taxi = map(int, input().split())
#sortedTaxi = sorted(enumerate(taxi), key = lambda x: x[1], reverse=True)
#ans = zip(sortedPas, sortedTaxi)
#sortedAns = sorted(ans, key=lambda x: [0][0])
#print(*map(lambda x: x[1][0] + 1, sortedAns))
#=====================================================================================
#pas = map(int, input().split())
#sortedPas = sorted(enumerate(pas), key = lambda x: x[1])
#taxi = map(int, input().split())
#sortedTaxi = sorted(enumerate(taxi), key = lambda x: x[1], reverse=True)
#ans = zip(sortedPas, sortedTaxi)
#sortedAns = sorted(ans, key=lambda x: [0][0])
#print(*map(lambda x: x[1][0] + 1, sortedAns))
#=====================================================================================
#import itertools
#print(*itertools.combinations([1,2, 3], 2))
#=====================================================================================
#import itertools
#print(*itertools.permutations([1,2, 3])) # перестановки
#=====================================================================================
#import itertools
#print(*itertools.permutations([1,2, 3], 2))
#=====================================================================================
#import itertools
#print(*itertools.combinations_with_replacement([1,2, 3], 2))
#=====================================================================================
#import functools

#prints = functools.partial(print, end=' ')
#prints(1)
#prints(2)
#=====================================================================================
#import functools

#print(functools.reduce(lambda x, y: x +y, [1, 2, 3]))
#=====================================================================================
#import itertools

#print(*itertools.accumulate([1, 4, 3, 5], max))
#=====================================================================================

#n = int(input())
#peopleList = map(int, input().split())
#peoples = sorted(list(enumerate(peopleList), key=lambda x: x[1]))
#taxiList = map(int, input().split())
#taxis = sorted(list(enumerate(taxiList)), key=lambda x: x[1], reverse=True)
#ans = sorted(zip(peoples, taxis), key=lambda x: x[0][0])
#print(*map(lambda x: x[1][0] + 1, ans))
#=====================================================================================
#def myRange(n):
#    i = 0
#    while i < n:
#        yield i
#        i += 1

#s = 0
#for i in myRange(100):
#    s += 1
#print(s)
#=====================================================================================
def myRange(n):
    i = 0
    while i < n:
        yield i**2
        i += 1

for i in myRange(10):
    print(i)








































