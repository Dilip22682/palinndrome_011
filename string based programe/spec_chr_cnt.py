s1="I! am@#$$#  loop!@#&^ @#@^loopdead Bad^$ guys@$ @#!!ot $@##llik"
s2=""
count=0
s3=s1.split()
print(s3)
for i in s3:
    # print(i,end=" ")
    for j in i:
        print(j,end=" ")
        if j in "!@#$%^&*":
           count+=1
        
    print()
    #    if count>3:
    #        s2+=j[::-1]
        
# print("\n",count)
print(s2)
    