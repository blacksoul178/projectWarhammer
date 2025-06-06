import config
import random




def attack_roll(attacks, units, weapon_skill, attack_modifier=0): #attacks modifier to implement when im sure how they work 😂
    if attacks < 1: 
        print("Attacks must be 1 or higher") #break if attacks < 1
        return
    if units < 1 : 
        print("Must have at least 1 unit attacking") 
        return
    if (weapon_skill < 1 or weapon_skill >6): 
        print("Weapon skill must be between 1-6") 
        return

    total_dices = attacks*units  #how many dice to rolls = how many units are attacking multiplied by how many attacks they do
    roll_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} 
    hits = 0 #hit counter
    
    print("")
    print("***** Start of roll *****")
    print(f"{units} units doing each {attacks} attacks, total dice count: {total_dices}")
    
    for i in range(total_dices):
            dice = random.randint(1,6)        #d6 rolling
            roll_count[dice] += 1   #increment dictionary
            if config.full_detail == True:         # Lists all attack dices once by one if option is on
                print(f"Dice {i+1} : {dice}")
            if dice >= weapon_skill: #if dice is higher than or equal to the hit counter, increment the hit count (for simplified rolls)
                hits += 1 
            
    
    if config.full_detail == True:      #if True, will return all dices count, even if zero
        for roll in roll_count:     
            print(f"{roll} : {roll_count[roll]}")  
    else:
        for roll in roll_count: ## returns the dice count if they are not 0
            if roll_count[roll] > 0:
                print(f"{roll} : {roll_count[roll]}")
    
    print("***** End of roll *****")    
    print(f"attacks of {weapon_skill} or higher hit")
    print(f"total hits: {hits} ")
        