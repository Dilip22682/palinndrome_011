

s1=input("Enter the Name:")
s2=""
i=0
while i<len(s1):
    # print(s1[i])
    k1=ord(s1[i])
    print("Ascii Value ->", s1[i],"=>",k1)
    bn=bin(k1)
    print(bn)
    i+=1