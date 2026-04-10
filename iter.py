l1=[1,2,3,4,6,7,8,9,11]
# l2=[x for x in range(0,10)]

# for i in l1:
#     if i not in l2:
#         print(i)
#         break


# for i in range(len(l1)-1):
#     if i+1!=l1[i]:
#         print(i+1)
#         break

for i in range(len(l1)-1):
    if l1[i+1]-l1[i]!=1:
        print(i+1)
        