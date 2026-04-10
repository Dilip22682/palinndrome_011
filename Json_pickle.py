import json
import pickle


# json

# with open("user.json", "w") as fk:
    
#     data={
#         "name": "Dilip patel",
#         "age": 23,
#         "Addresses":"basawangudi"
#     }
#     value=json.dump(data,fk)
#     print("data is dumpped",value)

# with open("user.json","r") as fk:
#     data=json.load(fk)
#     print("before modify data=>",data)
#     data["age"]=15
#     data["Addresses"]="Banglore"
#     print("after modify the data=>",data)



# pickle
data={
        "name": "Dilip patel",
        "age": 23,
        "Addresses":"basawangudi"
    }
# with open("user2.pickle","wb") as pk:
#     send=pickle.dump(data,pk)
#     print("data to be dumpped",send)

with open("user2.pickle","rb") as pk:
    send=pickle.load(pk)
    print("before data modify =>",send)
    send["name"]="Akash"
    send['age']=45
    print("After data modify =>",send)
    # print(send)
    
   
