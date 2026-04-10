# l1=[10,20,30,75,86,69,52,11]
# m=l1[0]
# s=l1[0]
# for i in l1:
#     if i>m:
#         m=i
#     elif i<s:
#         s=i
        
# print("maximum no:",m)
# print("minimum no:",s) 

l1=[10,20,78,34,56,78,6]
l1.sort(reverse=True)
print(l1)
sl=l1[0]
for i in l1:
    if i==sl:
        continue
    elif i<sl:
        print("second largest value:",i)
        break
    
