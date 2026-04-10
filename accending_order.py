
l1=[1,5,2,8]
res1=[]
temp=l1[-1]
for i in range(len(l1)-1):
    # print(l1[i],end=' ')
    if l1[i] > l1[i+1]:
        for j in range(l1[i],l1[i+1],-1):
            # print(j,end=' ')
            res1.append(j)
    
    
    # if l1[i] < l1[i+1]:
    else:
        for j in range(l1[i],l1[i+1],1):
            # print("else part:",j,end=' ')
            res1.append(j)
            
res1.append(temp)
print(res1)