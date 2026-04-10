k="TSorting123456"
u_c=""
l_c=""
ev=""
o=""
res=""
for i in k:
    if i.isnumeric():
        # print(i)
        if int(i)%2==0:
            print("even",i,type(i))
            ev+=i
        else:
            print("odd",i,type(i))
            # o.append(i)
            o+=i
    else:
        if i.isupper():
            # print(i)
            u_c+=i
        else:
            # print("cap",i)
            l_c+=i
        
                
p=['s','o','g','j','w'] 
print("bol na bsdk", p.sort())       
print(l_c)
print(u_c)
print(o)
print(ev)
print(l_c+u_c+o+ev)