a=int(input("a:"))
b=int(input("b:"))

print(f"before swap\n a:{a} \n b:{b} ")

# a,b=b,a
# print(f"after  swap\n a:{a} \n b:{b} ")

#2. temprory variables

# d=a+b
# b=d-b
# a=d-a
# print(f"after swap\n a:{a} \n b:{b}")

#3. using multiplication and division  a=5, b=3
# a=a*b
# b=a//b
# a=a//b

# print(f"after  swap\n a:{a} \n b:{b} ")


#4. using NOR gate operation
a=a^b
b=a^b
a=a^b

print(f"after  swap\n a:{a} \n b:{b} ")




