#utf-8
#r = range(0, 25)
#print(list(r))
#=======================================================================================================================
# Транспонирование матрицы
matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

# Транспонирование
matrix_t = list(zip(*matrix))

print(matrix_t)
# for x in matrix:
#     print(x)
#     print(sum(x))
#     print(min(x))
#     print(max(x))
# for line in matrix_t:
#     print(line)
print('*' * 25)

# for num, line in enumerate(matrix, 1):
#     print(num, line)
# for num, line in enumerate(matrix): # enumerating each string in this turtle or list
# for num, line in enumerate(matrix, 1):
#     print(f'№{num}:{line}')









