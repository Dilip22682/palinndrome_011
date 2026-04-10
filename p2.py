# alpha=[x for x in range(65,91)]
# print(alpha)

# alpha=[chr(x) for x in range(65,91)]
# print(alpha)
# alphabet=[]
# for x in range(97,123):
#     alphabet.append(chr(x))
#     print(chr(x),end=" ")
# print()    
# print(alphabet)
    
    
# alpha=tuple((chr(x) for x in range(65,91)))
# k=alpha
# print(alpha)

# s1={chr(x) for x in range(65,91)}
# # s12=s1
# print(s1)

# s1={x:x**2 for x in range(1,11)}
# print(s1)


# s12={chr(x):x for x in range(65,91)}
# print(s12)
# l1=[10,52,63,85,56,95,85,54,74,102,13,40]
# t_num=5
# l2=[]
# k1=l1.count(85)
# print("count:",k1)
# # print(max(l1))
# for i in l1:
#     if i>t_num:  # comparing the list number
#         t_num=i
#         l2.append(t_num)
        
# print(t_num)
# print(l2)
# l3=l2[-2:-3:-1]
# # l3=l2[::-1]
# print("height number:",t_num)
# print("Second Height no.:",l3)
# for i in l3:
#     print(l3,type(l3))
    
# l1=[10,52,63,85,56,95,85,54,74,102,13,40]
# l1.sort()
# l1.reverse()
# print(l1)


# def add():
#     a=int(input("a:"))
#     b=int(input("b:"))
#     # print(a+b)
#     return a+b
# jk=add()
# # obj=add(int(input("a:")),int(input("b:")))
# # print("sum:",obj )
# print("sum:",jk)


# p=0
# c=0

# i=0
# while i<5:
#     print("P times Win=>",p)
#     print("C times Win=>",c)
#     player=input("player:")
#     com=input("com:")
#     # print("i:",i)
#     if player==com:
#         print("Draw !!!")
#     elif player>com:
#         print("Player won the game!!!")
#         p+=1
#     else:
#         print("Computer won the game!!!")
#         c+=1
        
#     i+=1
#     print()
    




# p = 0
# c = 0

# for i in range(5):
#     player = input("player:")
#     com = input("com:")

#     if player == com:
#         print("Draw !!!")
#     elif player > com:
#         print("player won the game!!!")
#         p += 1
#     else:
#         print("com won the game!!!")
#         c += 1

# print("Final Results:")
# print("Player Wins:", p)
# print("Computer Wins:", c)

# if p > c:
#     print("Overall Winner: Player!")
# elif c > p:
#     print("Overall Winner: Computer!")
# else:
#     print("Overall Result: It's a Draw!")


# def check(k):
#     res=[] 
#     for i in k:
#         # print(i)
#         res.append(i)
#     m=set(res)
#     for j in m:
#         if j=="w":
#             return(f"{j}")
# k="Swiss"
# print(check(k))



# def check_str(str1,sub_str):
#     for i in range(len(str1)):
#         # print(str1[i])
#         # print( str1[i:i+len(sub_str):1])
#         if str1[i:i+len(sub_str)]==sub_str:
#             return f"sub string Found=>{str1[i:i+len(sub_str)]}  "
#         # else:
#         #     continue
    
#     return False

# str1="HelloWorld"
# sub_str="World"

# print(check_str(str1,sub_str))



# def fizzBuzz(n):
#     # Write your code here
#     for i in range(1,n,1):
#         print(i)
#         if i%3==0:
#             return "Fizz"
#         elif i%5==0:
#             return "Buzz"
#         elif i%3==0 and i%5==0:
#             return "FizzBuzz"
#         else:
#             return i
# print(fizzBuzz(int(input("num:"))))

# def fun(n):
#     for i in range(1,n+1,1):
#             # print(i)
#             if i%3==0 and i%5==0:
#                 print("FizzBuzz")
#             elif i%3==0:    
#                 print("Fizz" )    
#             elif i%5==0:
#                 print("Buzz")
#             else:
#                 print(i)
            
            
# num=int(input("num:"))            
# fun(num)

# def simpleArraySum(ar):
#     # Write your code here
#     c=0
#     c1=0
#     # for i in range(len(ar)):
#     for j in ar:
#         # return i
#         # print(ar[i],type(i))
#         # c+=ar[i]
#         c1+=j
#     return c1
#     print(c,type(c))
    
# l1=[100,2,3,4,10,11]
# print(simpleArraySum(l1))
    
# a=10
# b=20 
# res=[]
# res.append(a)    
# res.append(b)
# print(res,type(res))    
# # print(sum(l1))

l1=[1,2,3,4,5,6]
l2=l1.copy()
l2[0]="man"
print(l1[0],"=>",id(l1[0]))
print(l1)
print(l2[0],"=>",id(l2[0]))
print(l2)
    
    