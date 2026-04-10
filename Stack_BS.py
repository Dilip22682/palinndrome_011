def fun():
    print("i am fun ")
    fun1()
    print("bye--->fun")
def fun1():
    print("i am fun1 ")
    fun2()
    print("bye--->fun1")
def fun2():
    print("i am fun2")
    fun3()
    print("bye--->fun2")
def fun3():
    print("i am fun3")
    print("bye--->fun3")

fun()