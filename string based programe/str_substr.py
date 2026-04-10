# s1='abc defgh ijk lmno'
# s2="ijk"

# k1=s1.split(" ")
# print(k1)

# for i in k1:
#     if i==s2:
#         print("Substring is matched")
#         break
        
# else:
#     print("Substring is not matched")


# 2nd method 
# def match_substring(s1,s2):
#     for i in range(len(s1)):
#         if s1[i:i+len(s2)]==s2:
#             return f"{s1[i:i+len(s2)]} substring found"
#     return "substring not found"


# s1="HelloWorld"
# s2="World"
# print(match_substring(s1,s2))



# 3rd method
def check_str(str1,sub_str):
    for i in range(len(str1)):
        # print(str1[i])
        # print( str1[i:i+len(sub_str):1])
        if str1[i:i+len(sub_str)]==sub_str:
            # return f"sub string Found=>{str1[i:i+len(sub_str)]}  "
            return True
        # else:
        #     continue
    
    return False

str1="HelloWorld"
sub_str="World"

print(check_str(str1,sub_str))


    