# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
my_set = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    cmd , n = input().split()
    set_N = set(map(int,input().split()))
    getattr(my_set,cmd)(set_N)
print(sum(my_set))
