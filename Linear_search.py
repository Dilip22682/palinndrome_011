l1=[10,50,80,-3,100,75,11]
key=int(input("key:"))
for i in range(len(l1)):
    # print(l1[i])
    if l1[i]==key:
        print(f"{key} is found in the index at {i}" )
        break
else:
    print(f"{key} is not found in the index ")
    
# 2.nd method using linear search
    
# l1=[10,50,80,-3,100,75,11]
# key=int(input("key:"))
# found=False
# for i in range(len(l1)):
#     # print(l1[i])
#     if l1[i]==key:
#         print(f"{key} is found in the index at {i}" )
#         found=True
#         break
# if not found:
# # if key  not in l1:  # its simple if condition 
#     print(f"{key} is not found in the list")
    
    