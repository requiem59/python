import numpy
numpy.set_printoptions(legacy = '1.13')

print(numpy.eye(8, 7, k = 1))    # 8 X 7 Dimensional array with first upper diagonal 1

print(numpy.eye(8, 7, k = -2))   # 8 X 7 Dimensional array with second lower diagonal 1

n = int(input())
m = int(input())

print(numpy.eye(n, m, k = 0))