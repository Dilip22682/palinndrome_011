info={"name":"Dilip","Age":24,"loc":"Banglore","State":"Karanataka","phone":8858479389}
# print(info.keys()) # its give keys from the dictionary
# print(info.values(),type(info.values()))  # it gives values from dictionary
# t1=info.get("phone","not found")  # get buildin method direct unpack value in to its corresponding datatypes
# print(t1,type(t1))

# print(info.items())     # it return key and value from the dictionary in the for of tupple format , so for unpacking we can use for loop


for i,v in info.items():
    print(i,v,type(i),type(v))
    if v==info["phone"]:
        # print(info["phone"])
        print(f"{v} yes phone no. is matched")
        break
else:
     print("no phone no. matched")
        
        
# print(info.get("phone"))       # get buildin method direct unpack value in to its corresponding datatypes
# if keys not it return None whlie (info["phone"]) method return Error

# print(info["phone"],type(info["phone"]))
print()

