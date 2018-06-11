import numpy
N = input()
A = []
B = []
for i in range(N):
    A.append(map(int, raw_input().split()))
for i in range(N):
    B.append(map(int,raw_input().split()))
#A = numpy.array(A)
#B = numpy.array(B)

print numpy.dot(A , B )


