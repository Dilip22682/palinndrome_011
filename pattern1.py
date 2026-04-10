# star printing in Reverse order

# for i in range(5,1,-1): #line for row
#     for j in range(1,i):# line for column
#         print("*", end=' ')
#     print() 

# star printing in normal order

# for i in range(1,6,1): #line for row
#      for j in range(1,i+1):# line for column
#          print("*", end=' ')
#      print() 


# right angle triangle
r=int(input("r:"))
for i in range(6):
    for k in range(1, 6-i ):
        print(" ",end=' ')
    for j in range(1,i+1,1):
        print("*",end=' ')
    print() 


