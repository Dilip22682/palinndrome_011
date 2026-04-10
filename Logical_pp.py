#foctors of n numbers

# n=int(input("n:"))
# if n>0:
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")
            
#foctors of n numbers and also to count no. of loops

n=int(input("n:"))
c=0
if n>0:
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
            c=c+1
    print("\n" ,"no. of loops run:",c)
