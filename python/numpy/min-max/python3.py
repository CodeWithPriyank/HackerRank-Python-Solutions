import numpy  

n , m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

print(numpy.max(numpy.min(numpy.array(arr),axis=1)))


