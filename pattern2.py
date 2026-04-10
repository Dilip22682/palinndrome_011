#1. right angle triangle

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
    
    
# print("&"*20)


# # 2.right angle triangle opposite face
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
    
    
# 3. right angle triangle with white space here we need three loops 

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
            
#     print()
# print("5"*51)
# ##4. right angle triangle of opposite face with white space here we need three loops

# for i in range(5,0,-1):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")    
#     print()
    
    
# here we draw pyramid shape with white space here we need three loops

# r= int(input("row:"))

# for i in range(1,r):
#     for k in range(1,r-i):
#         print(" ",end=" ")
#     for j in range(1,(2*i-1)+1):
#         print("*",end=" ")

#     print()
        


#reverse order        
r= int(input("row:"))

for i in range(r,0,-1):
    for k in range(0,r-i):
        print(" ",end=" ")
    for j in range(1,(2*i-1)+1):
        print("*",end=" ")

    print()

