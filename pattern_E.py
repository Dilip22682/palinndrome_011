# n=7
# for row in range(n):
#     for col in range(n):
#         if row==0 or row==n-1 or row==n//2 or col==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
a=10
b=20
a,b=b,a
print(a,b)