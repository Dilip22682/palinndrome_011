x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
n=int(input("n:"))
result=[]
for i in range(x+1):
    # print(i)
    for j in range(y+1):
        # print(j)
        for k in range(z+1):
            if i+j+k !=n:
                result.append([i,j,k])
           
print(result)