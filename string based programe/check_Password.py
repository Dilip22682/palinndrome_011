def str_pass(s1):
    lc_c=0
    uc_c=0
    sp_c=0
    num=0
    if len(s1)>=8 and len(s1)<=30:
        if s1[0] not in "0123456789": # first character is not to be number
            for i in range(len(s1)):
                if s1[i]>'a' and s1[i]<'z':
                    lc_c+=1
                elif s1[i]>'A' and s1[i]<'Z':
                    uc_c+=1
                elif s1[i]>'0' and s1[i]<='9':
                    num+=1
                else:
                    sp_c+=1
        else:
            print("Password should not start with number, plz try again !!")
        if sp_c>=1 and num>=1 and uc_c>=1 and lc_c>=1:
            print("It's Valid Password ")
        else:
            print("It's Invalid Password")
    else:
        print("this can not be a valid password")
            

s1=input("Enter your password:")
str_pass(s1)