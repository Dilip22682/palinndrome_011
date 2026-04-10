s1="Everything Is Happening For A Reason"
s2=""
s2+=chr(ord(s1[0])+32)
for i in range(1,len(s1)):
    if s1[i]==" ":
        s2+="_"
    else:
        if s1[i-1]==" ":
            s2+=chr(ord(s1[i])+32)
        else:
            s2+=s1[i]
            
print(s1)
print(s2)