# Anagram = Another string that contains the same characters and make different words , only the order of characters can be different 
#   eg. "act"="cat"

l1=["eat","tea","tan","ate","nat","bat"]
q1=[]
q2=[]
q3=[]


for i in l1:
    for j in i:
        if j in ('a','e','t'):
            q1.append(i)
        elif j in ('a','t','n'):
            q2.append(i)
        else:
            q3.append(i)
print(q1)
print(q2)
print(q3)



# print(round(10/3, 10))
# print(round(10/3, 2))

# def rev(n):
#     s=0
#     n=str(n)
#     for i in range(-1, -len(n)-1, -1):
#         print(int(n[i]),end="")

# n=153
# rev(n)

# def rev(n):
#     s=0
#     while n>0:
#         d=n%10
#         s=s*10+d
#         n=n//10
#     return s

# n=153
# res=rev(n)
# print(res)



## fabinacci series using iterator

# def fab(n):
#     a,b=0,1
#     print(a,b,end=" ")
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
# n=10
# fab(n)
  
  
  
# num = 10
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n1 = n2
#     n2 = n3
#     n3 = n1 + n2
#     print(n3, end=" ")

# print()

