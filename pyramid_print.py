row=int(input("Enter row no.:"))
col=int(input("Enter column no.:"))
l=len(str(col*row))
val=1

for i in range(row):
    for j in range(col):
        print(str(val).zfill(l),end=" ")
        val+=1
        
    print()
    
    # for i in range(row):
    # for j in range(col):
    #     print(val,end=" ")
    # print()