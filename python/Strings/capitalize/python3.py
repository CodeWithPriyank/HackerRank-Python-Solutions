

# Complete the solve function below.
def solve(s):
    name= list(map(str,s.split(" ")))
    for i in range(len(name)):
        name[i]=name[i].capitalize()
        s=' '.join(name)
    return s
