import numpy 

arreglo = numpy.array([2, 4, 6, 8, 10, 12])

arreglo2 = arreglo * 10

print("{0} * 10 = {1}".format(arreglo, arreglo2))

arreglo3 = numpy.array([[2, 4, 7, 9], [1, 5, 3, 8], [6, 4, 8, 3]])
print(arreglo3)

print("tamaño de arreglo3 = {0}".format(arreglo3.size))

print("Elemento (2,1) de arreglo3 = {0}".format(arreglo3[2, 1]))