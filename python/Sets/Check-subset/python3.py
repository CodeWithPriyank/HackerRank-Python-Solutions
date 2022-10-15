# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())): 
    ele_a = int(input())
    set_a = set(map(int,input().split()))
    ele_b = int(input())
    set_b = set(map(int,input().split()))
    print(set_a.issubset(set_b))
