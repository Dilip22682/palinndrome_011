# r=int(input("r:"))
# c=int(input("c:"))
# val=r
# l=len(str(val))
# for i in range(r):
#     for j in range(c):
#         print(str(val).zfill(l),end=" ")
#     print()
#     val-=1
    
# r=int(input("r:"))
# c=int(input("c:"))
# # val=r
# for i in range(r+1,0,-1):
#     for j in range(i+1):
#         print(j,end=" ")
#     print()

# r=int(input("r:"))
# c=int(input("c:"))
# val=c
# l=len(str(val))
# for i in range(r):
#     for j in range(c):
#         print(str(val).zfill(l),end=" ")
#         val-=1
#     print()
#     val=c

# r=int(input("r:"))
# c=int(input("c:"))
# # l=len(str(val))
# for i in range(r):
#     val=c

#     for j in range(c):
#         print(val,end=" ")
#         val-=1
#     print()
    
    

    


# k=888
# h=str(k)
# temp=""

# for i in range(-1,len(h)-1,1):
#     print(h[i])
#     temp+=h[i]
    
# print(temp,type(temp))

# if int(temp)==k:
#     print("Palindrome")
# else:
#     print(" not a Palindrome")


# print(155%10)
# temp=k
# s=0
# while k>0:
#     rem=k%10  # it gives last digit from the given value
#     s=s*10 + rem
#     # print("start ")
#     k=k//10
#     # print("dilip")
# print(s) 

# if s==temp:
#     print("Palindrome")
# else:
#     print(" not a palindrome")



# def compareTriplets(a, b):
#     # Write your code here
#     res=[]
#     alice=0
#     bob=0
#     print(alice,bob)
#     for i,j in zip(a,b):
#         if i>j:
#             print("Alice:",i)
#             alice+=1
#             print(alice)
#         elif j>i:
#             print("Bob:",j)
#             bob+=1
#             print(bob)
#         else:
#             alice+=0
#             bob+=0
   
#     return alice,bob
# l1=[17,28,30]
# l2=[99,16,18]
# print(compareTriplets(l1,l2))
# txt = "ompany12"

# k=txt[0].isalnum()

# print(k)

# def solve(s):
#     print(s[0].upper())
#     if s[0].isalpha()==True:
#         s[0].upper()
#         print(s[0])
#     for i in range(1,len(s)):
#         if i==" ":
#             s[i+1].upper()
#     return s
# print(solve("hello world"))




# l1=[[1,2,3],[4,5,6],[7,8,9]]
# l2=[]
# for i in l1:
#     l2.extend(i)
# print(l2)


# def solve(s):
#     # l1=s.split()
#     # print(l1)
#     s1=s[0].upper()
#     # print(s1)
#     str1=""
#     for i in range(len(s)):
#         # print(s[i],end="")
#         if i==" ":
#             str1+=s[i+1].upper()
#             print(s[i+1])
#         else:
#             str1+=s[i]
#     print(str1)

# print(solve("hello world"))

# N = int(input("num:"))
# lst=[]
# lst.insert(0,5)
# lst.insert(1,10)
# lst.insert(0,6)
# lst.remove(6)
# # lst.remove(9)
# lst.append(1)
# print(lst)


# x=lambda n:n
# print(x(5))



# num=int(input())
# t1=[]
# for i in range(num+1):
#     t1.append(i)
    
# print(hash(tuple(t1)))

# n=int(input())
# t = tuple(map(str, input().split()))
# print(hash(t))
# n=5
# m=2
# # A=[input("str") for i in range(n)]
# # print(A)
# # from collection import defaultdict 
# # d=defaultdict(list)
# # A=[input("str1:") for i in range(n)]
# A=['a', 'a', 'b', 'a', 'b']
# B=['a', 'b']
# # B=[input("str2") for j in range(m)]
# print(A)
# print(B)

# for i in B:
#     for j in A:
#         if i==j:
#             # print(j+1)
#             print()
#         else:
#             print(-1)
            


# def fun(n):
#     if n==0:
#         return f"hello world 0"
#     else:
#         print(f"{n}")
#         return fun(n-1)
# print(fun(5))  



# def factorial(n):
#     # if n==0:
#     #     return 1
#     # print("n value:",n)
#     # return factorial(n-1)*n
#     s=1
#     print(n)
#     for i in range(1,n+1):
#         s=i*s
#         print(s)
#         print("i:",i)
#     return s

# print(factorial(25)) 


# from math import sqrt
# # def fun(a,b):
# #     return len([x for x in range(int(sqrt(a)//1), int(sqrt(b)//1)+1) if x**2 >= a and x**2 <= b])
# # t=fun(4,9)
# # print(t)
# print(sqrt(4))


# def reverse_words_order_and_swap_cases(sentence):
#     # Write your code here
#     # print(sentence[::-1])
#     l1=sentence.split()
#     # print(l1)

#     k1=""
#     print(type(k1))
#     for i in range(-1,-len(l1)-1,-1):
#         # k1.join(l1[i])
#         # print(l1[i])
#         k1+=" "
        
#     # # for i in sentence:
#         for j in l1[i]:
#             print(j)
#             if j>="a" and j<="z":
#                 k1+=chr(ord(j)-32)
#                 # print("cap=>",chr(ord(j)-32))
#             elif j>="A" and j<="Z":
#                 k1+=chr(ord(j)+32)
#                 print("small=>",chr(ord(j)+32))
#             else:
#                 k1+=(j)
#     # print(k1+" ")
#     return(k1)
# sentence="aWESOME is cODING"    
# l1=reverse_words_order_and_swap_cases(sentence)
# print("jkhsdah:",l1)



# def staircase(n):
#     # Write your code here
#     # k=1
#     # for i in range(n):
#     #     # print(n,type(n))
#     #     print(" "*(n-i) + "#"*i)
#     # print()
# staircase(6)

# def staircase(n):
#     for i in range(1, n + 1):
#         # Print the spaces: (n-i) spaces
#         print(' ' * (n - i), end='')
#         # Print the hashes: i hashes
#         print('#' * i)
# staircase(6)


# def find(l1):
#     lst=[]
#     for i in range(len(l1)):
#         s=0
#         # print(l1[i])
#         for j in str(l1[i]):
#             s+=int(j)
#             lst.append(s)
#             print("ss:",s,type(s))
#         print()
#     print("sum:",s)
#     print(lst)


# l1=[12,34,11,14]
# res=find(l1)
# print(res)

# for i in range(1,10):
#     print(i,end="")
# else:
#     print("hello world")


# def sum_list(n):
#     if len(n) == 0:
#         return 0
#     return n[0]+sum_list(n[1:])
# res = sum_list([2,4,6,1,2,9,9])
# print(res)








