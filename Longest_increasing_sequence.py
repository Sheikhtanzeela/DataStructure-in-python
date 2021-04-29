def lis(arr):
    n = len(arr)
    lit = [1]
    for i in range(1,n):
        lit.append(1)
        for j in range(0,i):
            if arr[i]>arr[j] and lit[i]<=lit[j-]:
                lit[i] = lit[j]+1
    print(lit)
    return max(lit)
print(lis([3,2,4,5,1,7]))
