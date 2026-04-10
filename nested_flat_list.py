
l2=[[10,20,[1,3],[1,2,[3,4,[1,2]]]]]
# res=[]
# def fun(l2):
#     for i in l2:
#         if isinstance(i,list):
#             fun(i)
#         else:
#             res.append(i)
# fun(l2)
# print(res)

# 2. method to converting nested list into flatter list

# res1=[]
# while l2:
#     i=l2.pop(0)  # here pop will delete the value and return it into i
#     # print(i)
#     if isinstance(i,list):
#         l2=i+l2
#     else:
#         res1.append(i)
# print(res1)

    
    
    

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))

    
# 3. method to converting nested list into flatter list using recursion


# class TELEPHONE:
#     def __init__(self,postpaid):
#         self.postpaid = postpaid


#     def outgoing(self):
#         print('Calling...Waiting')


#     def incoming(self):
#         print('Ringing')


# class MOBILE(TELEPHONE):
#     def __init__(self, postpaid,prepaid,camera,chat):
#         super().__init__(postpaid)
#         self.prepaid = prepaid
#         self.camera = camera
#         self.chat = chat


   
# m1 = MOBILE(599,299,'Yes','Yes')
# print(m1.postpaid)  # 599
# print

class A:
    def method1(self):
        print('Class A')
class B(A):
    def method2(self):
        print('Class B')
class C(B):
    def method2(self):
        print('Class C')
        super().method2()


o1 = C()
o1.method1() # Class A
o1.method2()
