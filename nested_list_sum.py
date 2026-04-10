# l1=[[1,2,3],[10,15,20],[4,5],100]
# res=0
# for i in l1:
#     if isinstance(i,list):
#         for j in i:
#             res+=j
#     elif isinstance(i,(int,float)):
#         res+=i
        
# print(res)



# 2nd largest num

# l1=[10,2,50,3,4,-4,8]
# m=max(l1)
# res=0
# for i in l1:
#     if res<i and res> m:
#         res=i
              
# print("2nd largest num:",res)


l1=[10,"don",1.5,-3,(1+2j),"kham",43,8]


for i in range(len(l1)-1,-1,1):
    if  l1[i]==int and l1[i]>l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
        
    print(l1)
        
        
        