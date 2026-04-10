# dict1={input("keys:"):int(input("value:")) for i in range(5) }
# print(dict1)

def test(n):
    d1={}
    for i in range(n):
        d1[input("keys:")]=int(input("value:"))
    return d1

print(test(3))