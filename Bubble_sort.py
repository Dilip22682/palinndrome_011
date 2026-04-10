# l1=[50,40,30,20,10]
# for i in range(len(l1)-1,0,-1):
#     # print(l1[i])
#     if l1[i]>l1[i-1]:
#         l1[i]=l1[i-1]
#         print(l1[i-1])
#     else:
#         print(l1[i])
        
        
        
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
# n = int(input("n:"))

# lis = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
# print(lis)

for i in range(x + 1):
    print(i)
for j in range(y + 1):
    print(j)
for k in range(z + 1):
    print(k)
l1=[i,j,k]
print(l1)