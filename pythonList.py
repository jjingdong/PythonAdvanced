#Eg
matrix = [[i for i in range(0, 10)] for j in range(0, 10)]
print(matrix)
matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

#Eg
matrix = [[0 for i in range(2)] for j in range(10)]
print(matrix)
matrix = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

#Eg
matrix = [['-' for i in range(3)] for j in range(3)]
print(matrix)
matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

#Eg
array = [None for _ in range(10)]
print(array)
array = [None, None, None, None, None, None, None, None, None, None]

#Eg
array = [None] * 10
print(array)
array = [None, None, None, None, None, None, None, None, None, None]

#Eg
array = [0 for i in range(10)]
print(array)
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Eg
array = [0] * 10
print(array)
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Eg
array = [i for i in range(1, 10)]
print(array)
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Eg
matrix = [[0 for i in range(0, 3)] for j in range(0, 3)]
matrix[0][0] = 1
matrix[1][0] = 1
matrix[2][0] = 1
print(matrix)

def checkCols():
    i = 0
    j = 0
    temp = 1
    for j in range(3):
        if matrix[i][j] != temp:
            return False
        i += 1

    return True
print(checkCols())


