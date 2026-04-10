def add(n):
    if n == 0:
        return 0
    else:
       return n+add(n-1)
       
print("start:")
print(add(int(input("n:"))))
print("end")
    