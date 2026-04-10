# sum of even digit number using while loop
n=int(input("n:"))
if n>0:
    c=0
    while(n>0):
        rem=n%10
        if rem%2==0:
            c+=rem
        rem/=10
    print(c)
            