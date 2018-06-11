"""
import numpy
N,M = map(int,raw_input().split())
arr = []
for i in range(M):
    arr.append(map(float,raw_input().split()))
print numpy.mean(arr, axis = 1)
print numpy.var(arr, axis = 0)
print numpy.std(arr)
"""
import numpy

N, M = map(int, raw_input().split())

my_array = numpy.array([ map(int, raw_input().split()) for i in range(N) ])
#Below line was added as the numpy used for generating the output was v1.13 and current version is v 1.14

numpy.set_printoptions(legacy='1.13')

print numpy.mean(my_array, axis = 1)
print numpy.var(my_array, axis = 0)
print numpy.std(my_array, axis = None)
