for row in range(6):
    for col in range(4):
        if ((row==0 or row==5) and (col!=3)) or ((col==0 or col==3 ) and (row!=0 and row!=5)) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# k=4
# for row in range(k):
#     for col in range(k):
#         if  (row==0 or row==k-1) or (col==0 or col==k-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# n = 5

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()