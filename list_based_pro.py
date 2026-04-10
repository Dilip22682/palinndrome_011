def happy(array,m):
    # n=int(input())
    # for i in range(len(n)+1):
    #     array=int(input())
        
    # # m=int(input())
    for j in range(len(m)+1):
        A=set(int(input()))
        B=set(int(input()))
        
    happiness=0

    for i in array:
        if i in A:
            happiness+=1
        elif i in B:
            happiness-=1
        else:
            continue
    return happiness