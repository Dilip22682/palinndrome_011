# left Rotation
# in-[1,2,3,4]
# op->[2,3,4,1]
list1=[]
l2=[10,20,30,40]
temp=l2[0]
# print(temp,type(temp))
# temp2=l2[-1]
for i in range(1,len(l2),1):
        # print(l2[i])
        list1.append(l2[i])
        
list1.append(temp)
print(list1)