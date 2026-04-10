# def leapyear(year):
    
#         if (year%4==0 and year%100!=0): 
#             return f"{year} is a leap year"
#         elif year%400==0 and year%100==0:
#             return f"{year} is a leap year"
#         else:
#             return f"{year} is not a leap year" 
   
# res=leapyear(int(input("Enter the year:")))
# print(res)
       
       
def leap(n):      
    
    # if(n%400==0) or (n%400==0 and n%100==0):
    if(n%400==0) or (n%4==0 and n%100!=0):
        print("leap year ")
    else:
        print("not leap year")
m=int(input("Year:"))
leap(m)