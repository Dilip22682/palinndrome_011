# l1=[1,2,5,8,9,1,10]
# l1.sort()
# print(l1)
# maxi=l1[-1]
# mini=l1[0]
# max_c=0
# min_c=0
# # tmp_min=0
# # tmp_max=0
# for i in range(len(l1)):
#     # print(l1[i],end=" ")
#     if l1[i]==maxi:
#         max_c+=1
#     elif l1[i]==mini:
#         min_c+=1
#     elif l1[i]>mini:
#         continue
#     elif l1[i]<maxi:
#         continue
# print()
# print( "maximum value occurance :",max_c )
# print("minimum value occurance :", min_c )
# # print(maxi,mini)
        
        
    
l1="Today is Badday ever seen".split()
o={}
p={}
l={}
for i in l1:
    o[i]=i[1::2][::-1]
    p[i]=len([j for j in i if j in 'aeiouAEIOU'])
    
    
# for k in l1:
#     c=[]
    
#     for n in range(1,len(k),2):
#         # print(n,end=" ")
#         c+=[n]
#     # print(sum(c))
#     l[k]=sum(c)
for k in l1:
    l[k] = sum(i for i in range(1,len(k),2))    
print(l)  
# print(o,p,sep='\n\n')

# print(l1[:2:-1])
     

    
