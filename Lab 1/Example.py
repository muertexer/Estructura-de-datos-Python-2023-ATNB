# este codigo es netamente para hacer practicas antes de ser agregado al codigo oficial (los ejercicios)


result_list = []
for i in range(10):
    result_list.append(hash(i) % 10+1)
print(result_list)

result_list = []
for i in range(5):
    result_list.append(hash(i) % 5+1)
print(result_list)



import numpy as np

matrix = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        matrix[i][j] = hash(i+j) % 10
print(matrix)