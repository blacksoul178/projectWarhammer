from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random


#variables used for dice rolls

#Options:
full_detail = True #Return full dice rolls if Set to true, else will simply return the desired values (values that hit/wound/save)

#Stats related to attack rolls:
weapon_skill = 3  #WS
attacks_number = 3  #A
units_attacking = 3 #number of units attacking    
attack_modifier = 0

#Stats related to wound rolls:
strength = 0  #S
armor_pen = 0  #AP
toughness = 0  #t


#UI

class DiceRollerApp(App):
     
    def build(self):
        attack_roll_button = Button(text="Attack roll!",
                      background_color =("gray"),
                      font_size=150)       
        attack_roll_button.bind(on_press=self.click_attack_roll_button)      
        return attack_roll_button
      
    def click_attack_roll_button(self, instance):
        attack_roll(attacks_number, units_attacking, weapon_skill, attack_modifier)  
    


#Dice rolling and reporting functions

def attack_roll(attacks, units, weapon_skill, attack_modifier=0): #attacks modifier to implement when im sure how they work 😂
    if attacks < 1: 
        print("Attacks must be 1 or higher") #break if attacks < 1
        return

    total_dices = attacks*units  #how many dice to rolls = how many units are attacking multiplied by how many attacks they do
    roll_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0} 
    hits = 0 #hit counter
    
    for i in range(total_dices):
            dice = random.randint(1,6)        #d6 rolling
            roll_count[dice] += 1   #increment dictionary
            if full_detail == True:         # Lists all attack dices once by one if option is on
                print(f"Dice {i+1} : {dice}")
            if dice >= weapon_skill: #if dice is higher than or equal to the hit counter, increment the hit count (for simplified rolls)
                hits += 1
    
    
            
            
    print("***** Start of roll *****")
    for roll in roll_count:
        print(f"{roll} : {roll_count[roll]}")
    print("***** End of roll *****")    
    print(f"attacks higher than {weapon_skill} hit")
    print(f"total hits: {hits} ")
        
            
        
        
    
    
    

if __name__ == "__main__":
    DiceRollerApp().run()