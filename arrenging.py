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
    
# print(int_l+float_l+com_l+bool_l+str_l)

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


# 2.questions

# new_lst=[8,7,20,50,14,3]
# l=[]
# sum=0
# for i in new_lst:
#     c=0
#     # print(i)
#     for j in range(1,i+1):
#         if i%j==0:
#             c=c+1
#             # print("i:",i,end=" ")
#             # print("c:",c,end=" ")
#             # print()
            
#     if c==2:
#         l.append(i)
#         sum+=i
# # print(l)
# print("prime no. list :",l)
# print("sum of prime number:",sum)




# 3. question

# l1=["man",3.55,"don","patel", "khan",100]
# l12=[]
# for i in l1:
#     if type(i)==float:
#          i=str(i)
         
#          l12.append(i)
#     elif type(i)==int:
#          i=str(i)
#          l12.append(i)
#     elif type(i)==complex:
#         l12.append(i)
#     elif type(i)==complex:
#         l12.append(i)
#     else:
#          l12.append(i)
        
# # print(l12)    
    
# dict={}
# for k in l12:
#      dict.update({k:len(k)})
# print(dict)
 

# l3=eval(input("m:"))
# s=0
# for i in l3:
#     if i>1:
#         for j in range(2,i//2+1):
#             i%j==0
#     else:
#         s+=1
# print(s)
    
             
# l=abs(-100-5.2)
# print(l)

l6=[4,5,6,6]
sum=l6[0]+l6[1]
print(sum)