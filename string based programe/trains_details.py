
class TRAINS:

    def get_train_name(self,train_no):
        for i in trains_details:
            if i.value()==p1:
                return name.value()
            
            
    def get_running_trains_of_the_day(self,work_day):
        global train_details
        data=[]
        for train in trains_details:
            if work_day in train['Working_days']:
                data.append(train['name']+ " "+str(train['train_no']))
        if data:
            return data
        else:
            return "train not found"
        
    def get_train_price(self,train_no,passengers):
        global trains_details
        for train in trains_details:
            if train_no==train['train_no']:
                total_price =train["ac-Sleeper"]*passengers["ac-Sleeper"]+train["sleeper"]*passengers["sleeper"]
                return total_price
    
trains_details=[
    {"name": "karnataka Express","train_no":16432,"from":"Bangalore","to":"Mangalore","Working_days":["Mo","Tu","We","Th","Fr","Sa"],"ac-Sleeper":800,"sleeper":450},
    {"name": "Chennai Express","train_no":12672,"from":"Bangalore","to":"Chennai","Working_days":["Mo","We","Fr"],"ac-Sleeper":1000,"sleeper":500},
    {"name": "Delhi Express","train_no":12658,"from":"Delhi","to":"Bangalore","Working_days":["Mo","Tu","We","Fr","Su"],"ac-Sleeper":850,"sleeper":400},
    {"name": "Delhi Express","train_no":12650,"from":"Delhi","to":"Bangalore","Working_days":["Mo","We","Fr","Su"],"ac-Sleeper":900,"sleeper":350},
    {"name": "Danapur Special Express","train_no":30252,"from":"Bangalore","to":"DDU","Working_days":["Tu","We"],"ac-Sleeper":1100,"sleeper":600},
]
# get_train_name(int(input("train no.:")),train_details)
t1=TRAINS()
print(t1.get_running_trains_of_the_day("Mo"))
print(t1.get_train_price(train_no:12658,passenger:8))
