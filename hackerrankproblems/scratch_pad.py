if __name__ == '__main__':
    n = int(input())
    [print(y) for y in list(map(lambda x: x**2, filter(lambda x: x<n, range(n))))]
    [print(y) for y in (list(filter(lambda x: x < n**2, map(lambda x: x**2, range(n)))))]
    [print(y) for y in list(map(lambda x: x**2 if x < n else None, range(0, n)))]

    arr = [1,2,3,4,5,6,7,8]
    a = 3
    b = 7
    k = 100
    print([x + k if i in range(a,b) else x for i,x in enumerate(arr)])