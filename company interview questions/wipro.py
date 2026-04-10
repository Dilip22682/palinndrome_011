# def oddeven(l1):
#     l2=[]
#     i=0
#     while i<len(l1):
#         if l1[i]%2==0:
           
#         else:
#             print("odd:",l1[i])
#         i+=1

#     print("l2:",l2)

# l1=[12,15,88,96,53,32,55]
# res=oddeven(l1)
# print(res)


# def miniMaxSum(arr):
#     # Write your code here
#     # print(arr)
#     mx=0
#     mn=0
#     for i in range(len(arr)):
#         print(i)
#         mn+=arr[i]
#         mx+=arr[i]
#     mx=mx-arr[0]
#     print("max:",mx)
#     mn=mn-arr[len(arr)-1]
#     # print(len(arr))
#     print("min:",mn)
#     return mn,mx

# arr=[1,2,3,4,5]
# th=miniMaxSum(arr)
# print(th)

def hello(**args):
    print(args,type(args))
   
    
    
h=hello(l=input("b:"),c=20,d=50,op=566)
print(h)