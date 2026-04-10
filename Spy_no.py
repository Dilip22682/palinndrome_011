# num=123
# sum of digits=1+2+3=6
# product of digits=1*2*3=6
# sum of all the digit of the num is equal to the product of all the digit of that number is called spy  number

n=int(input("n:"))
temp=n
s=0
p=1

while n>0:
    rem=n%10
    s+=rem
    p*=rem
    n//=10
print("sum of digits:",s)
print("product of digits:",p)    
if s==p:
    print(f"{temp} is a spy number")
else:
    print(f"{temp} is not a spy number")
