from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from functools import partial
import random

from roll import attack_roll
from attack_properties import AttackProperties

#variables used for dice rolls

#Options:
attack_data = AttackProperties() #importing AttackProperties values 



#Stats related to wound rolls:
strength = 0  #S
armor_pen = 0  #AP
toughness = 0  #t


#UI

class DiceRollerApp(App):
     
    def build(self):
        attacks_layout = BoxLayout(orientation='horizontal', spacing=10) #Create box 
        
        
        attacks_count = Label(text="Attacks ⚔",font_size=48)   #attacks label
        attacks_layout.add_widget(attacks_count)    #add to layout 
        
        
        self.attacks_input = TextInput(text=str(attack_data.attacks_number),
                                       input_filter="int",
                                       multiline=False)
        attacks_layout.add_widget(self.attacks_input)   
        
        self.attacks_input.bind(text=self.on_attacks_input_text)  #live updating
        attack_data.bind(attacks_number=self.on_attacks_number_change)
        
        
        attacks_increment_button = Button(text="+",         #increment button
                                          background_color =("gray"),
                                          color="green",
                                          font_size=24)
        attacks_increment_button.bind(on_press=partial(self.click_increment_button, self.attacks_input))
        attacks_layout.add_widget(attacks_increment_button)
        
        
        attacks_decrement_button = Button(text="-",         #decrement button
                                          background_color =("gray"),
                                          color="red",
                                          font_size=24)
        attacks_decrement_button.bind(on_press=partial(self.click_decrement_button, self.attacks_input))
        attacks_layout.add_widget(attacks_decrement_button)
        
        
        attack_roll_button = Button(text="Attack roll!",        #attack roll button 
                      background_color =("gray"),
                      font_size=24)       
        attack_roll_button.bind(on_press=self.click_attack_roll_button)
        attacks_layout.add_widget(attack_roll_button)
              
        return  attacks_layout #attack_roll_button
      
    
    



  
        
        
    def on_attacks_input_text(self,instance, value):    #real time updating values
        if value.isdigit():
            if instance is self.attacks_input:
                attack_data.attacks_number = int(value)
            # elif instance is self.units_input:
            #     attack_data.units_attacking = int(value)
            
    def on_attacks_number_change(self,instance, value):
        # Avoid recursive update
        if self.attacks_input.text != str(value):
            self.attacks_input.text = str(value)
        
        
            

###buttons binding###


    def click_attack_roll_button(self, instance):       #attack rolling call function
        attack_roll(attack_data.attacks_number, attack_data.units_attacking, attack_data.weapon_skill, attack_data.attack_modifier)  
        
    def click_increment_button(self, increment_area, instance): #increment button action
        match increment_area :
            case self.attacks_input:
                attack_data.attacks_number  += 1
            # case self.units_input:
            #     attack_data.units_attacking += 1
            # case self.weapon_skill_input:
            #     attack_data.weapon_skill += 1
            # case self.attack_modifier_input:
            #     attack_data.attack_modifier += 1
            
        
    def click_decrement_button(self, decrement_area, instance): #decrement button action and conditionals
        match decrement_area :
            case self.attacks_input:
                if attack_data.attacks_number <= 1:
                    attack_data.attacks_number = 1
                    return
                attack_data.attacks_number -= 1
                
            # case self.units_input:
            #     if attack_data.units_attacking <= 1:
            #         attack_data.units_attacking = 1
            #         return
            #     attack_data.units_attacking -= 1

            # case self.weapon_skill_input:
            #     if attack_data.weapon_skill <= 1:
            #         attack_data.weapon_skill = 1
            #         return
            #     attack_data.weapon_skill -= 1
            
        
        
    
    
    

if __name__ == "__main__":
    DiceRollerApp().run()