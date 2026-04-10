#  QES.1 first reverse it and then find the sum of even no. position  of no. and return the value using static class methods.
# s1={10,23,30,55,90,30,60}


# for _ in range(len(s1)):
#     el=max(s1)
#     k=s1.remove(el)
#     # k=s1.discard(el)
#     print(el,type(el))
#     # print(k)


# master code for set

# s = {1, 2, 3}
# for _ in range(len(s)):
#     elem = max(s)
#     s.remove(elem)
#     print(elem,end=" ")
#     # print(elem, end=',' if s else '')
    




# 2nd method
s1={10,23,30,55,90,30,60}
l1=list(s1)
print(l1)

# evensum=0
# even_list=[]
# for i in range(len(l1)):
#     # print(l1[i])
#     if i%2==0:
#         # print(l1[i])
#         print(i)
#         even_list.append(l1[i])
       
# print(even_list)
# print("sum of even place values:",sum(even_list))
# # print(evensum)
        
    







# # QES.2  find student Qaulified or not
# n1=6   # no. of subject
# n2=6   # no of subject
# s1=[24,19,45,26,18,48]  # score first sem
# s2=[15,40,25,26,13,42] # score second sem
# class TestCase(object):
#     @classmethod
#     def is_qualified(cls,n1,n2,s1,s2):
#         pass

# TestCase.is_qualified ()