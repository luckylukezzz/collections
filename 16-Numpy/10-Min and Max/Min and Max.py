#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
import numpy
n,m=map(int,input().split())
ar=numpy.array([input().split() for i in range(n)],int)
print(numpy.max(numpy.min(ar,axis=1)))

