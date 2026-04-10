# def foo(fname,val):
#     print(fname(val))
# foo(max,[1,2,3])
# foo(min,[1,2,3])
# # print(q)
# def foo(i, x=[]):
#     x.append(i)
#     return x
# for i in range(3):
#     print(foo(i))
    
    
#     x = 50
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is now', x)


# printing prime number 

# n1=int(input("n:"))
# n2=int(input("n:"))


# # if n1<n2 & n1>0 & n2>0:
# for i in range(n1,n2+1):
#     c=0
#     # print(i,end=" ")
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print(i,end=" ")
        
        
# printing sum of number , which has increasing power as moving next digit right direction
# n=int(input("Enter the number:"))
# c=1
# sum=0
# for i in str(n):
#     # print(i,end=" ") 
#     sum=sum+int(i)**c
#     c+=1
# print(sum,end=" ")

# using while loop
# i=0
# while i<100:
#     if i%2==0:
#         print(i,end=",")
#     i+=1
    
# To count the number of factor of a number
# n=int(input("n:"))
# c=0
# if n>0:
#     for i in range(1,n+1):
#         if n%i==0:
#             print("factors",i)
#             c+=1
#     print("no. of loops:",c) 
#     if c==2:
#         print(f"{n} is prime no")    
#     else:
#         print(f"{n} is not a prime no")   


# n=int(input("n:"))
# c=0
# if n>0:
#     for i in range(1,n/2+1):
#         if n%i==0:
#             print("factors",i)
#             c+=1
#     print("no. of loops:",c) 
#     if c==0:
#         print(f"{n} is prime no")    
#     else:
#         print(f"{n} is not a prime no")   
        
# n=input()   
# rev=n[::-1] 
# if n==rev:
#     print(f"{n} is palidrome no")
# else:
#     print(f"{n} is not palidrome")

# row=int(input("n:"))
# col=int(input("c:"))
# for i in range(row):
#     for j in range(col):
#         print("8", end=" ")
#     print()

# def close_far(a, b, c):
#   if (c==a+1 or c==a-1) and (b==a+1 or b==a-1):
#     return False
#   elif b==a+1 or b==a-1:
#     return True
#   elif c==a+1 or c==a-1:
#     return True
#   else :
#    return False
        
        
# obj=close_far(1,2,3)
# print(obj)

# a=10
# b=20
# def add():
#     global b
    
#     a=100
#     b=50
# add()
# print(a)
# print(b)

# a="abcdefg"
# i="a"
# while i in a:
#     print(i)
#     break


# for i in [1,2,3,4,5][::-1]:
#     print(i,end=" ")

# n=int(input("m:"))
# print(n,type(n))



# num=int(input("n:"))
# s=len(str(num))
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num//=10
# print(sum,end=" ")
# digit_sum=0
# for i in str(sum):
#     digit_sum=digit_sum+int(i)   
# if s==digit_sum:
#     print(f"{num} is super digit number")
# else:
    # print(f"{num} is not a super digit number")
    
    
# sum13([1, 2, 13, 2, 1, 13])
    
# def has22(nums):
#   for i in range(len(nums)):
#     if nums[i]==2 and nums[i+1]==2:
#       return True    
#     else:
#       return False

# obj=has22([1, 2, 8,5,6])
# print(obj)

# sum of list  using iterable methods
# l1=[10,20,30]

# sum=0
# for k in l1:
#   sum+=k
# print(sum)
    
    
  # using range method
  
# l1=[10,20,30,5.2,7.22,(2+9j),"don"]
# int_l=[]
# float_l=[]
# com_l=[]
# bool_l=[]
# str_l=[]
# ord_lst=[]
# for i in l1:
#   if type(i)==int:
#     int_l.append(i)
#   elif type(i)==float:
#     float_l.append(i)
#   elif type(i)==complex:
#     com_l.append(i)
#   elif type(i)==bool:
#     bool_l.append(i)
#   else:
#     str_l.append(i)
    
# # print(com_l)

# for j in int_l:
#   ord_lst.append(j)

    
# for j in float_l:
#   ord_lst.append(j)
# # print(ord_lst)

# for j in com_l:
#   ord_lst.append(j)
# # print(ord_lst)

# for j in bool_l:
#   ord_lst.append(j)
# # print(ord_lst)

# for j in str_l:
#   ord_lst.append(j)
# print(ord_lst)

# x = int(input("x:"))
# y = int(input("y:"))
# z = int(input("z:"))
# n = int(input("n:"))

# lis = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
# print(lis)
# l1=[]
# for i in range(x + 1):
#   print(i)
#   for j in range(y + 1):
#     print(j)
#     for k in range(z + 1):
#       print(k)


# s = 'abracadabra'
# def test(s,char1,pos):
#   return s[:pos]+char1+s[pos+1:]


# res=test(s,"k",5)
# print(res)


# lst=[]
# for _ in range(int(input("num:"))):
#       name = input()
#       score = float(input())      
#       lst.append([name,score])
# print(lst)
p=[['a', 62.0], ['d', 8.0], ['f', 77.0]]

as_list=[] 
for j in p:
  print(j)
  print(j[1])
  as_list.append(j[1])
    
print(as_list.sort())



    

  
  
  










         
        