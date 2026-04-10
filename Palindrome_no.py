# num=int(input("n:"))
# num=1234560
# n=int(input("n:"))
# print(n,type(n))
# rev=n[::-1]
# print(rev,type(rev))
# if rev==n:
#     print(f"{n} is palindrome number")
# else:
#     print(f"{n} is not palindrome number")



# # 2nd method 
# n=111
# temp=n
# s=0
# while n>0:
#     rem=n%10
#     print("Rem:",rem)
#     s=s*10+rem
#     n=n//10
# print(s)
# print("n:",n)
# if s==temp:
#     print(f"{temp}  is palindrome")
# else:
#     print(f"{temp} is not palindrome")    


# print(n%10)

     



# palindroem is or not


# num=111111
# # i=len(s1)
# temp=num
# i=len(str(num))
# pali=""
# while i > 0:
#     rem=num%10
#     print(rem, end=' ')
#     # print(i, end=' ')
#     pali+=str(rem)
#     num=num//10
    
#     i-=1
# print("\n",pali,type(pali))
# print(num,temp)


# if temp==int(pali):
#     print("palindrome")
# else:
#     print("not a palindrome")






def fab(k):
    # a,b=0,1
    if k==0:
        return 1
    else:
        return k*fab(k-1)

res=fab(5)
print(res)
    


a,b=0,1
for _ in range(150):
    print(a,end=" ")
    a,b=b,a+b
    
    
    
    
    
def cab(k):
    # a,b=0,1
    if k==0:
        return 1
    else:
        return k*cab(k-1)

res=cab(5)
print(res)
    
    
    
def sab(k):
    # a,b=0,1
    if k==0:
        return 1
    else:
        return k*sab(k-1)

res=sab(5)
print(res)
