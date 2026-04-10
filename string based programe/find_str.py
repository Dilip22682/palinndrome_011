def str_list(s1,sub_str):

    l1=[]
    new_str=s1.split(" ")
    
    for i in range(len(new_str)):
        # print(new_str[i])
        if new_str[i]==sub_str:
            l1.append(new_str[i])
            l1.append(i)
    return l1
        
    
s1="Fred fed Ted bread and Ted Fed Fred bread and Ted Fred Fed bread to Thread"
sub_str=input("Enter substring: ")

res=str_list(s1,sub_str)
print(res)

    
    

    