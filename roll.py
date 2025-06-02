import config
import random




def attack_roll(attacks, units, weapon_skill, attack_modifier=0): #attacks modifier to implement when im sure how they work 😂
    if attacks < 1: 
        print("Attacks must be 1 or higher") #break if attacks < 1
        return

    total_dices = attacks*units  #how many dice to rolls = how many units are attacking multiplied by how many attacks they do
    roll_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} 
    hits = 0 #hit counter
    
    print("***** Start of roll *****")
    print(f"{units} units doing each {attacks} attacks, total dice count: {total_dices}")
    
    for i in range(total_dices):
            dice = random.randint(1,6)        #d6 rolling
            roll_count[dice] += 1   #increment dictionary
            if config.full_detail == True:         # Lists all attack dices once by one if option is on
                print(f"Dice {i+1} : {dice}")
            if dice >= weapon_skill: #if dice is higher than or equal to the hit counter, increment the hit count (for simplified rolls)
                hits += 1 
            
    for roll in roll_count:
        print(f"{roll} : {roll_count[roll]}")
    print("***** End of roll *****")    
    print(f"attacks higher than {weapon_skill} hit")
    print(f"total hits: {hits} ")
        