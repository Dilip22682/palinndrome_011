n=int(input("n:"))
if n>0:
    c=0
    for i in range(2,n+1):
        if n%i==0:
            print(i,end=" ")
            c+=1
    print()
    print("no. of loop:",c)
    if c==2:
        print(f"{n} is a prime no.")
    else:
        print(f"{n} is not a prime no.")




# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(3))
        