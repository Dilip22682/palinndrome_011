s1="abc"
s2="xyz"
str3=""

for i in range(len(s1)):
    str3+=s1[i]+s2[len(s2)-i-1]
        
    
    
print(str3)