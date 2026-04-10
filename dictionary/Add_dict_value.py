def Add_dict(d1):
    res=0
    for i,k in d1.items():
        print(i,k)
        # print(i.values())
        if isinstance(k,int):
        # if k.values()==int:
            res+=k
    return "Addition result:=",res



d1={
    "one":500,
    167:10,
    "python":1,
    "Banglore":"city",
    "numpy":35+8j,
    74:"two",
    "java":1.5,
    "Django":"10",
    70:100
}
print(Add_dict(d1))