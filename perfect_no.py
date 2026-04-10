# perfect number= all positive divisor of a number except itself
# eg.  6=1,2,3      sum=1+2+3=6
n=int(input("n:"))
sum=0
for i in range(1,n):
   if n%i==0:
       sum=sum+i
       print(f"factor of {n}:",i,end=" \n")
print("sum:",sum)
if sum==n:
    print(f"{n} is perfect number")
else:
    print(f"{n} is not perfect number")
