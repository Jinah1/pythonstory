def Alone():
    print("You have decided to go alone.")
    arrival()
    
def Explore():
    print("You explore your urges, and find yourself drawn to the attic. Once there, a glint in a dark corner of the room catches your eye. You go to investigate, and find a large tuba. Suddenly, an idea invades your thoughts. With a sly grin, you take the tuba, and start heading down stairs.")

def Play():
   
def Ride():
    print("You have decided to ride with friends.")

def beginning():
    travel=input("You are Chad, and you've been invited to a party hosted by the renowned Arj! You have two ways to get there: walk by yourself, or get a ride there. What will you do? Please type 'Alone' or 'Ride' ")
    if (travel== 'Alone' or travel=='alone'):
        Alone()
    elif (travel=='Ride' or travel== 'ride'):
        Ride()
    else:
        print("I do not understand")
        beginning()
    
def arrival():
    travel=input("You arrive at the party, and are greeted by Arj. Arj leaves you and you find yourself alone. Overwhelmed by an urge to explore, you wonder if doing so will yield positive results. You can 'explore' your curiosity, or you can 'play' party games with Arj.")
    if (travel == "explore" or travel == "Explore"):
        Explore()
    elif(travel == "play" or travel=="Play" or travel=="Games"):
        Play()
    else:
        print("Please enter correctly")
        arrival()
    
def activity():
    party=input("You arrive at the party, and are greeted by Arj. You can 'play' party games with Arj.")
    if party=='games' or 'play' or 'Play':
        print("You arrive at the party, and are greeted by Arj. He invites you to play party games with him, and you don't have any reason to argue. You feel like you've missed something, but it's probably not important.")
    
beginning()




"""TUBA"""
"""
print("The reckless teens partying downstairs look at you with a puzzled look on their faces.")
print("As everyone became quiet, you quickly climb on to the milk pong table and blow into the mouthpiece with all your might.")
print("A random bystander intrigued by your amazing skills, pulls out his own tuba from his pocket and plays along with you.")
print("As the night goes on, more and more people take out their tubas and begin having battles and tournaments.")
print("After having the best night of your life, you along with your new friends went home happily.")
"""
"""MILK PONG"""
"""
print("Arj takes you over to the milk pong table and you decide to place an evil bet with him. The Winner must kill the Loser!")
print("Arj being the party monster he is, believes he will easily win. You on the other hand have never played milk pong before and wish you never placed this bet with him.")
    YOU WIN: print("You miraculously defeat Arj through a hard fought battle, and must now execute him. It is a difficult thing to do, but you have no choice as it was a bet. After taking his life, you decide to take all of his wealth for yourself.")
             print("Using the wealth to hire elite criminals from around the globe, you take over the U.S. government and become a dictator.")
    YOU LOSE: print("Arj's skills are much past your level causing you to be defeated. Arj, with pity for his good friend, kills you to fulfil the bet.")
              print("After entering the afterlife, you come back to haunt Arj forever in his dreams.")
"""