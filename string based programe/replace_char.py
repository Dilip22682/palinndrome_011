def re_char(s1,c1,pos):
    # return s1[:pos]+c1+s1[pos+1:]
    s3=''
    
    for i in range(len(s1)):
        # print(s1[i])
        if i==pos:
            s3+=c1
        else:
            s3+=s1[i]
    return s3
            
    


s1="abracadabra"
c1=input("Enter a character:")
pos=int(input("Enter a position:"))

k1=re_char(s1,c1,pos)
print(k1)