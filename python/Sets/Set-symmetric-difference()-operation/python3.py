# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_news = int(input())
n = set(map(int,input().split()))
french_news = int(input())
b = set(map(int,input().split()))
print(len(n.symmetric_difference(b)))
