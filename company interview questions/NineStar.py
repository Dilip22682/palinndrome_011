# n=int(input("n:"))
# print(chr(n))
# print('alphabet' if chr(n) else 'non alphabet')

# d1={}
# for _ in range(0,5):
#     d1[input("key:")]=int(input("value:"))
# print(d1)

# try:
#     l1=[10,20,30,40,50]
#     # print(l1.index(4))
#     print(l1.pop())
#     print(l1.pop(2))
#     # print(l1.pop(6))
#     a=20
#     b=0
#     c=a/b
#     print(c)
# except IndexError as ie:
#     print("reason =>",ie)
# except ZeroDivisionError as ze:
#     print("reason =>",ze)
# except ValueError as ve:
#     print("reason =>",ve)


#tije conversion

# def timeConversion(s):
#     if s[-2:]=="AM":
#         # print(int(s[:2]),type(s))
#         if s[:2]==str(12):
#             print('00'+s[2:6])
#         else:
#             print(s[:8])
      
#     elif s[-2:]=="PM":
#        k=str(int(s[:2])+12)+s[2:8]
#        print(k)
#     elif int(s[3:5])==int:
#            print('00'+s[-8:-2])
       
# # s='07:05:45PM'
# s='10:05:45PM'
# # s='11:10:45PM'
# # s='12:05:45AM'
# s='07:05:45AM'
# # s='12:00:01AM'
# res=timeConversion(s)
# print(res)
        
        
        
# s = "Python"
# rev = ""

# for i in range(len(s)-1, -1, -1):
#     rev += s[i]
#     print(rev)

# print(rev)


s = "Dilip"
rev = ""

for ch in s:
    rev = ch + rev     
    # print(ch)
    print(rev)

print(rev)
