# l1=[10,20,3,40,50,60]
# l2=["a","b","c","d","e","f"]
# res=dict(zip(l1,l2))
# # res=tuple(zip(l1,l2))
# print(res,type(res))



l1=[10,20,3,40,50,60]
l2=[10,20,30,40,5,6]
k=zip(l1,l2)
print("zip form:",list(k))
# l=k.__iter__()
# m=0
# while m<=len(l1):
    
#     print("zip form www:",l.__next__())
#     m+=1


# l1=[]
# l2=[]
# for i in range(3):
#     l1.append(i)
# for j in range(3):
#     l2.append(j)
# print(dict(zip(l1,l2)))

# for l1,l2 in zip(l1,l2):
#     print(l1,l2,type(l1),type(l2))
    

# sq=tuple([square for square in range(1,11)])
# sq1=tuple((square for square in range(1,11)))
# print(sq)
# print(sq1)
# print(sq.__next__())
# print(sq.__next__())
# print(sq.__next__())
# print(sq.__next__())
# print(sq.__next__())
# print(sq.__next__())
# print(sq.__next__())

# while True:
#     if sq >11:
#      print(sq.__next__())
#      break
    
