# def happy(n,m):
#     n=int(input("len of array:"))
#     array=set()
#     for i in range(n):
#         array.add(int(input("array:")))
#     print("Array =",array)
        
#     m=int(input("len of sets:"))
#     A=set()
#     B=set()
#     for j in range(m):
#         A.add(int(input("A:")))
#         B.add(int(input("B:")))
        
#     print("set A =",A)
#     print("set B =",B)
#     happiness=0

#     for i in array:
#         if i in A:
#             happiness+=1
#         elif i in B:
#             happiness-=1
#         else:
#             continue
#     return "result is =>",happiness

# res=happy(3,2)
# print(res)




# m=int(input("len of sets:"))
# A=set()
# B=set()
# for j in range(m):
#     A.add(int(input("A:")))
#     B.add(int(input("B:")))

# print([1,4,5,4,8,6,8])


# counting stamp


# Enter your code here. Read input from STDIN. Print output to STDOUT
# def count_country(n):
#     c_stamp=set()
#     for _ in range(n):
#         name=input("name:")
#         c_stamp.add(name)
#     print(c_stamp)
#     return len(c_stamp)

# print(count_country(7))

l1=[6,8,2,9,6,]
s = set(map(int, input("num:").split()))
print(s)
