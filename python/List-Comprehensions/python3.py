if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list1 = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                list1.append([i,j,k])
                
    result = list(filter(lambda a:sum(a)!=n,list1))
    print(result)
