def fun(*args):
    print(args,type(args))
    
# fun("a"=10,"b"=20,"c"=30,"d"=40)  # throwing error 
fun(10,20,30,40,50)



def fun1(**args):
    print(args,type(args))
    
fun1(a=10,b=20,c=30,d=40)
# fun1()