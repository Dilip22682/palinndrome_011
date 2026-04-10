#panagram= all Alphabet should be present in single sentancen
s1="The Quick brown fox jumps over the a lazy dog"


# correct code
unique_char=set()
for i in s1:
    if i==" ":
        continue
    else:
        unique_char.add(i.lower())
        
# print(unique_char)
k1=list(unique_char)
k1.sort()
print(k1)
print(len(unique_char))

if len(unique_char)==26:
    print("string is paragram")



# s1="virat"
# s2="Anuksha"
# str2=""
# for i in range(len(s1)):
#     if i<len(s1)//2:
    
    
# print(s1[:3]+s2+s1[3:])

























    
    
    
    

