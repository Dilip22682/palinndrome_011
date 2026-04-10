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

l1=[10,50,80,-3,100,75,11,10,80,10,80,50]
key=int(input("key:"))
found=False
n=int(input("n:"))
c=0
for i in range(len(l1)):
    
    if l1[i]==key:
        c+=1
        if c==n:
            print(f"{n}th occurance of {key} found at index {i}" )
            found=True
            break
if not found:
# if key  not in l1:  # its simple if condition 
 print(f"{n}th occurance of {key} found at index")