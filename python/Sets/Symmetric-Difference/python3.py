# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
#another code
_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))
[print(i) for i in sorted(a.symmetric_difference(b))]
"""

M = int(input())
a = set(list(map(int,input().split(" "))))
N= int(input())
b=set(list(map(int,input().split(" "))))


result = list(a.symmetric_difference(b))
result.sort()
for _ in result:
    print(_)
