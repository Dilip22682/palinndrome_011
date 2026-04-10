# l1=[1,12,13,53,11]
# # l1[5,0,1]
# # l2=[]
# for i in l1:
#     if i==13:
#         i=0
# print(l1)
# 
# 
def swap_case(s):
    lst=s.split()
    s=[]
    word=""
    for i in lst:
        for j in i:
            # print(i,type(i))
            if j>="a" and j<="z":
                s. append(j.upper())
                # word+j.upper()
                # print(word)
            # print(s)
            elif j>="A" and j<="Z":
                s. append(j.lower())
                # word+j.lower()
                
            else:
                s.append(j)
                # word+j
                
    # print(word)   
    # str1=""
    # for i in s:
    #     str1+i
    # print(str1)            
    return s 
st="HackerRank.com presents Pythonist 2."
print(swap_case(st))