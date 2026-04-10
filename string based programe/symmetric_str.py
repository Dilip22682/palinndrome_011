# def symmetric(s1):
#     mid=len(s1)//2
# # count=0
#     if len(s1)%2==0:
#         if s1[:mid]==s1[mid:]:
#             return( "string is symmetric")
#         else:
#             return("string is not symmetric")
#     else:
#             return("string is not symmetric")
            
    
# s1="dilip"
# print(symmetric(s1))



s1=input("name:")
mid=len(s1)//2
s2=""
k=''

s2+=s1[mid-1:mid]
s2+=s1[mid:mid+2]
for i in s2:
    if i>="a" and i<="z":
        k+=chr(ord(i)-32)
    elif i>="A" and i<="Z":
        k+=chr(ord(i)+32)
print(k)
print(s1[:mid-1]+k+s1[mid+2:])

        
        