def max_populated_city(cities):
    city=""
    max=0
    for i,k in cities.items():
        print(i,k["populations"])
        if max<k["populations"]:
            max=k["populations"]
            city=i
    return cities[city]
        




cities={
    "Banglore":{
        "State":"Karanataka",
        "CM":"Siddaramaya",
        "populations":5462176,
        "places":["Lalbagh","Vindhansudha","Tippu summer palace"]
    },
    "Hydrabad":{
        "State":"AP",
        "CM":"Chandra babu naidu",
        "populations":6421634,
        "places":["Rajamolicity","Charminar","Hussainsagar","Tankbund road","Nickless road"]
    },
    
    "Chennai":{
        "State":"Tamilnadu",
        "CM":"Stalin",
        "populations":11068877,
        "places":["Marina Beach","ECR raod","Chepauk Stadium","Egmo Museum"]
    },
    
    "Varanasi":{
        "State":"Uttar Pradesh",
        "CM":"Yogi Adityanath",
        "populations":35514685,
        "places":["Assi Ghat","sarnath", "Vishwanath Temple","bharat Temple ","Rama nagar Qila"]
        
    },
    
     "Mumbai":{
        "State":"Maharastra",
        "CM":"Eknath Sindeh",
        "populations":55514685,
        "places":["Mumbai film city", "Marina Beach","Anlilia","india gate"]
        
    },
}

res=max_populated_city(cities)
print(res)
