n=int(input("n:"))
a=0
b=1
print(a,b,end=" ")
for i in range(0,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")



# # using iter method

# n=int(input("n:"))
# n=5
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(0,n):
#     c=a+b
#     a=b
#     b=c
#     # print(dir(c))
#     l=c.__iter__()
#     print(l.__next__())
    
    
    
 # using recursion method

# def fabrec(n):
#     if n<=1:
#         # print("hello")
#         return n
#     else:
#         return fabrec(n-1)+fabrec(n-2)

# l=int(input("lenght of fab series:"))
# for i in range(l):
#     print(fabrec(i),end=" ")
