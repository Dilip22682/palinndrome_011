# input_string = "This is a test. This test is only a test."

# # Convert the string to lowercase to ensure case-insensitive counting
# input_string = input_string.lower()

# # Initialize variables
# word = ""
# words = []
# counts = {}

# # Manually split the string into words
# for char in input_string:
#     if char.isalnum():
#         word += char
#     else:
#         if word:
#             words.append(word)
#             word = ""
# if word:
#     words.append(word)

# # Manually count the occurrences of each word
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1

# # Print the result
# print(counts)



# import time
# s = time.time()

# def sum_of_multiples_with_loop(n, limit):
#     total = 0
#     for i in range(n, limit, n):
#         total += i
#     return total

# # Calculate the sum of multiples of 5 and 3 limit is 1,00,00,000
# limit = 10000000
# sum_multiples_of_5 = sum_of_multiples_with_loop(5, limit)
# sum_multiples_of_3 = sum_of_multiples_with_loop(3, limit)

# # print(sum_multiples_of_5)
# # print(sum_multiples_of_3)
# print(sum_multiples_of_5 * sum_multiples_of_3)

# e = time.time()
# print(e - s)


# class A:
#     x=1
# class B(A):
#     pass

# class C(A):
#     x=2
# class D(B,C):
#     pass
# # o=D()
# print(D.x)

# import re
# def find(s1,s2):
    # for i in range(len(s1)):
        # print(s1[i])
        # print(len(s2))
        # print(s1[i:len(s2)+i:1])
        # print(s1[i+2:len(s2)+i:1])
        # if s1[i+2:len(s2)+i:1]=="BC":
        #     print(s1[i+2:len(s2)+i:1])
        # else:
        #      print("no match found")
    
    # return s1[i+2:len(s2)+i:1]
             
#         RES=pat=re.findall('A[A-Z]BC',s1)
#         # RES=pat=re.search('A[A-Z]BC',s1)
#         print("PATTERN found",RES)




# s1='ANSKIRKDPLGFAWBCKDAIBCN'
# s2="ASBC"
# print(find(s1,s2))
    
# l1=[1,2,3,4,8,9]
# print(set(map(lambda num:num*2,l1)))

# print(chr(65))
# l1=[]
# for i in range(ord("Z"),ord("A")+1,-1):
#     # print(chr(i),end=" ")
#     l1.append(chr(i))
# print(l1)    
# k1=l1.reverse()
# print(k1)
# print(ord("A"),type(ord("A")))

# lst=[chr(i) for i in range(ord("Z"),ord("A")-1,-1)]
# print(lst)

 