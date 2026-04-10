# o/p= 1,2,3,4,3,2,1

def fun1(n):
    if n<4:
        print(n,end=" ")
        fun1(n+1)
    print(n,end=" ")
        
print("Start")        
fun1(1)
print("\nEnd")