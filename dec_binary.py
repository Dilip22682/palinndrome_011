def decBin(n):
    if n==0:
        return n/2
        # decBin(n)

print(decBin(12))


# l1=[1,2,3]
# for i in range(len(l1)-1,-1,-1):
#     print(l1[i], end=' ')

# l1=[10,20,30,40,50,60,70,80,90]
# # # l2=l1[::-2]
# # # print(l2)
    
# # l1.reverse()
# # print(l1)

# def sum2(nums):
#   s=0
#   for i in range(0,len(nums),1):
#     s+=nums[i]
#   return s
# print(sum2([5,1,2,8]))


# def has23(nums):
#   for i in nums:
#     if i==2 or i==3:
#       return True
#     elif i>=4 or i<=1:
#         continue
#     else:
#       return False

# print(has23([4,3]))