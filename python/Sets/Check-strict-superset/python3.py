# Enter your code here. Read input from STDIN. Print output to STDOUT
 
temp, arr = set(), set(map(int, input().split()))
[temp.update(set(map(int, input().split()))) for _ in range(int(input()))]
print(arr.issuperset(temp))
