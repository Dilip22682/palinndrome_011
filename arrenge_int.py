# l1=[10,"don",1.5,-3,(1+2j),"khan",43,8]

# for i in range(len(l1)-1):
#     if isinstance(i,(float,int)):
#         for j in range(i+1,len(l1)-1):
#             # print(j,end=" ")
#             if isinstance(j,(float,int)):
#                 if l1[i]>l1[j]:
#                     l1[i],l1[j]=l1[j],l1[i]
# print(l1)


l2=[[10,20,[1,3],[1,2,[3,4,[1,2]]]]]
res=[]
def fun(l2):
    for i in l2:
        if isinstance(i,list):
            fun(i)
        else:
            res.append(i)
fun(l2)
# print(res)
res.sort()# arrenging accending order
print(res)
print(list(set(res))) # removing duplicates