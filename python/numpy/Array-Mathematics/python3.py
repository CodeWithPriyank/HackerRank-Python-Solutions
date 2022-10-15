import numpy

n, m = map(int, input().split())
a = [numpy.array(input().split(), int) for _ in range(n)]
b = [numpy.array(input().split(), int) for _ in range(n)]
functions = [numpy.add, numpy.subtract, numpy.multiply, numpy.floor_divide, numpy.mod, numpy.power]
[print(numpy.array(fn(a,b))) for fn in functions]
