# l1=[1,1,2,3,3,4,3,4,5,4,1,1]

# d1={}
# for i in l1:
#     if i in d1:
#         d1[i] +=1
#     else:
#         d1[i] =1
    
# print(d1)


def word_count(string):
  my_string = string.lower().split()
  my_dict = {}
  for i in range( len(my_string)):
    my_dict[my_string[i]] = my_string[i].count(my_string[i])
  print(my_dict)

word_count("I am that I am")