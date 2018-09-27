def Alone():
    print("You have decided to go alone.")
    return Alone
def Ride():
    print("You have decided to ride with friends.")
    return Ride


travel=input("You are Chad, and you've been invited to a party hosted by the renowned Arj! You have two ways to get there: walk by yourself, or get a ride there. What will you do? Please type 'Alone' or 'Ride'")
if (travel== 'Alone' or 'alone'):
    Alone()
    travel=True
elif(travel=='Ride' or 'ride'):
    Ride()
    travel=False


    
    
    
    
