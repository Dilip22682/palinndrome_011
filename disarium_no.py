# num= 175    A Disarium number is a number where the sum of its digits raised to their respective positions equals the number itself.
#k =1**1+7**2+5**3 => 1+49+125=175
# num==k then it is daisarium number

# is called Disarium number
n=input("n:")
l=1
sum=0
for i in n:
    i=int(i)**l
    l+=1
    sum+=i
    print("sum:",sum)
if sum==int(n):
    print(f"{n} Disarium number")
else:
     print(f"{n} is not a Disarium number")
