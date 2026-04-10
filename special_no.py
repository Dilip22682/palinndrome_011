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
l=s+p
print(s)
print(p)
print("sum of s+p:",l)
if s+p==temp:
    print(f"{temp} is special number")
else:
    print(f"{temp} is not special number")