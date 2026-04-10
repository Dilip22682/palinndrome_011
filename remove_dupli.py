# l1=[10,220,10,30,40,80,30]
# res=[]
# # for i in l1:
# #     if i not in res:
# #         res.append(i)
        
# # print(res)

# for i in range(len(l1)-1):
#     # print(l1)
#     for j in range(i+1,len(l1)):
#         if l1[i]==l1[j]:
#             l1[j]=None
#             # print(l1)
            
# # i=0
# # while i<len(l1):
# #     if l1[i]==None:
# #         i+=1
# #         continue
# #     else:
# #         print(l1[i])
# #     i+=1

# while None in l1:
#     l1.remove(None)
#     print(l1)
    
# print(l1)
    
    
    
l2=[10,50,80,-3,100,75,11]
num=int(input("n:"))
for i in range(len(l2)):
    if l2[i]==num:
        print(f"{num} is found inside the list at index of {i}")
        break
else:
    print(f"{num} is not inside the list")