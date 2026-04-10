num=int(input("n:"))
s=len(str(num))
print(s,type(s))
temp=num
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num//=10
print(f"{temp} sum of digits:",sum)
digit_sum=0
for i in str(sum):
    digit_sum=digit_sum+int(i)   
print(f"{sum} sum of digits:",digit_sum,end=" \n")
if s==digit_sum:
    print(f"{temp} is super digit number")
else:
    print(f"{temp} is not a super digit number")