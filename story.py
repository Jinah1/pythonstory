def Alone():
    travel=True
    print("You have decided to go alone.")
    return travel
def Explore():
    if party=='explore' or 'Explore':
        print("You explore your urges, and find yourself drawn to the attic. Once there, a glint in a dark corner of the room catches your eye. You go to investigate, and find a large tuba. Suddenly, an idea invades your thoughts. With a sly grin, you take the tuba, and start heading down stairs.")
    return Explore
def Play():
    if party=='games' or 'play' or 'Play':
        print("You arrive at the party, and are greeted by Arj. He invites you to play party games with him, and you don't have any reason to argue. You feel like you've missed something, but it's probably not important.")
    else:
        print("Perish")
def Ride():
    travel=False
    print("You have decided to ride with friends.")
    return travel

def beginniner():
    travel=input("You are Chad, and you've been invited to a party hosted by the renowned Arj! You have two ways to get there: walk by yourself, or get a ride there. What will you do? Please type 'Alone' or 'Ride'")
    if (travel== 'Alone' or travel=='alone'):
        Alone()
    elif (travel=='Ride' or travel== 'ride'):
        Ride()
    return travel    
#else:
    #print("That's incorrect.")
    
def travelling():
    while travel == True:
        party=input("You arrive at the party, and are greeted by Arj. Arj leaves you and you find yourself alone. Overwhelmed by an urge to explore, you wonder if doing so will yield positive results. You can 'explore' your curiosity, or you can 'play' party games with Arj.")
    if (party== 'explore' or party=='Explore'):
        Explore()
    elif (party== 'play' or party=='Play'):
        Play()
    while travel== False:
        party=input("You arrive at the party, and are greeted by Arj. You can 'play' party games with Arj.")
    if party=='games' or 'play' or 'Play':
        print("You arrive at the party, and are greeted by Arj. He invites you to play party games with him, and you don't have any reason to argue. You feel like you've missed something, but it's probably not important.")
    else:
        print("Perish")
    return party
    
travel = beginniner()   
party=travelling()