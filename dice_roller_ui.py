from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from functools import partial

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
        dice_roller = BoxLayout(orientation='horizontal', spacing=10) #Create box 
        
        
        ### Attacks Label
        
        attacks_layout_label = BoxLayout(orientation="vertical", spacing=10) #1st inner box so attacks label and input box stack one on top of the other,
        
        attacks_count_label = Label(text="Attacks",font_size=48)   #attacks label
        attacks_layout_label.add_widget(attacks_count_label)    #add to layout 
        
        self.attacks_input_box = TextInput(text=str(attack_data.attacks_number),    #input box
                                    input_filter="int",
                                    multiline=False)
        attacks_layout_label.add_widget(self.attacks_input_box)   
            
        self.attacks_input_box.bind(text=self.real_time_input_text)  #live updating logic
        attack_data.bind(attacks_number=self.on_attacks_number_change)
        
        
        ### Units Label
        
        units_layout_label = BoxLayout(orientation="vertical", spacing=10) #1st inner box so units label and input box stack one on top of the other,
        
        units_count_label = Label(text="Units",font_size=48)   #units label
        units_layout_label.add_widget(units_count_label)    #add to layout 
        
        self.units_input_box = TextInput(text=str(attack_data.units_number),    #input box
                                    input_filter="int",
                                    multiline=False)
        units_layout_label.add_widget(self.units_input_box)   
            
        self.units_input_box.bind(text=self.real_time_input_text)  #live updating logic
        attack_data.bind(units_number=self.on_units_number_change)
        
        attacks_layout_label.add_widget(units_layout_label)
        
        
        ### Weapon Skill Label
        
        weapon_skill_layout_label = BoxLayout(orientation="vertical", spacing=10) #1st inner box so weapon_skill label and input box stack one on top of the other,
        
        weapon_skill_count_label = Label(text="weapon skill",font_size=48)   #weapon_skill label
        weapon_skill_layout_label.add_widget(weapon_skill_count_label)    #add to layout 
        
        self.weapon_skill_input_box = TextInput(text=str(attack_data.weapon_skill),    #input box
                                    input_filter="int",
                                    multiline=False)
        weapon_skill_layout_label.add_widget(self.weapon_skill_input_box)   
            
        self.weapon_skill_input_box.bind(text=self.real_time_input_text)  #live updating logic
        attack_data.bind(weapon_skill=self.on_weapon_skill_change)
        
        attacks_layout_label.add_widget(weapon_skill_layout_label)
        

        
        
        ### Attacks adjustment buttons
        
        attacks_adjustment_buttons = BoxLayout(orientation="vertical", spacing=10) #2nd inner box so attacks increment buttons stacks atop one another
        
        attacks_increment_button = Button(text="+",         #increment button
                                          background_color =("gray"),
                                          color="green",
                                          font_size=24)
        attacks_increment_button.bind(on_release=partial(self.click_increment_button, self.attacks_input_box))
        attacks_adjustment_buttons.add_widget(attacks_increment_button)
        
        
        attacks_decrement_button = Button(text="-",         #decrement button
                                          background_color =("gray"),
                                          color="red",
                                          font_size=24)
        attacks_decrement_button.bind(on_release=partial(self.click_decrement_button, self.attacks_input_box))
        attacks_adjustment_buttons.add_widget(attacks_decrement_button)
        
        
        ### Units adjustment buttons
        
        units_adjustment_buttons = BoxLayout(orientation="vertical", spacing=10) #2nd inner box so attacks increment buttons stacks atop one another
        
        units_increment_button = Button(text="+",         #increment button
                                          background_color =("gray"),
                                          color="green",
                                          font_size=24)
        units_increment_button.bind(on_release=partial(self.click_increment_button, self.units_input_box))
        units_adjustment_buttons.add_widget(units_increment_button)
        
        
        units_decrement_button = Button(text="-",         #decrement button
                                          background_color =("gray"),
                                          color="red",
                                          font_size=24)
        units_decrement_button.bind(on_release=partial(self.click_decrement_button, self.units_input_box))
        units_adjustment_buttons.add_widget(units_decrement_button)
        
        attacks_adjustment_buttons.add_widget(units_adjustment_buttons) #add units adjusment buttons to the attacks adjustments
        
        
        ### weapon_skill adjustment buttons
        
        weapon_skill_adjustments_buttons = BoxLayout(orientation="vertical", spacing=10) #2nd inner box so attacks increment buttons stacks atop one another
        
        weapon_skill_button = Button(text="+",         #increment button
                                          background_color =("gray"),
                                          color="green",
                                          font_size=24)
        weapon_skill_button.bind(on_release=partial(self.click_increment_button, self.weapon_skill_input_box))
        weapon_skill_adjustments_buttons.add_widget(weapon_skill_button)
        
        
        weapon_skill_decrement_button = Button(text="-",         #decrement button
                                          background_color =("gray"),
                                          color="red",
                                          font_size=24)
        weapon_skill_decrement_button.bind(on_release=partial(self.click_decrement_button, self.weapon_skill_input_box))
        weapon_skill_adjustments_buttons.add_widget(weapon_skill_decrement_button)
        
        attacks_adjustment_buttons.add_widget(weapon_skill_adjustments_buttons) #add units adjusment buttons to the attacks adjustments
        
        
        
        ### Roll button
        
        attack_roll_button = Button(text="Attack roll!",        #attack roll button 
                      background_color =("gray"),
                      font_size=24)       
        attack_roll_button.bind(on_release=self.click_attack_roll_button)
        
        
        #dice_roller_2 = BoxLayout(orientation='horizontal', spacing=10)
        
        
        dice_roller.add_widget(attacks_layout_label) # add all 3 vertical text Input labels to the box layout
        dice_roller.add_widget(attacks_adjustment_buttons) # add all 3 vertical adjustments buttons to the box layout
        dice_roller.add_widget(attack_roll_button) # Add Attack roll button in the final column     
        
        return  dice_roller
      
    
    



        ### Real time input update logic
         
        
    def real_time_input_text(self,instance, value):    #real time updating values for attacks input
        if value.isdigit():
            if instance is self.attacks_input_box:
                attack_data.attacks_number = int(value)
            if instance is self.units_input_box:
                attack_data.units_number = int(value)
            if instance is self.weapon_skill_input_box:
                attack_data.weapon_skill = int(value)
            
    def on_attacks_number_change(self,instance, value):
        # Avoid recursive update
        if self.attacks_input_box.text != str(value):
            self.attacks_input_box.text = str(value)  
            
    def on_units_number_change(self,instance, value):
        # Avoid recursive update
        if self.units_input_box.text != str(value):
            self.units_input_box.text = str(value)       
            
    def on_weapon_skill_change(self,instance, value):
        # Avoid recursive update
        if self.weapon_skill_input_box.text != str(value):
            self.weapon_skill_input_box.text = str(value)                   

            
    
        
        
            

###buttons binding###


    def click_attack_roll_button(self, instance):       #attack rolling call function
        attack_roll(attack_data.attacks_number, attack_data.units_number, attack_data.weapon_skill, attack_data.attack_modifier)  
        
    def click_increment_button(self, increment_area, instance): #increment button action
        match increment_area :
            case self.attacks_input_box:
                attack_data.attacks_number  += 1
            case self.units_input_box:
                attack_data.units_number += 1    
            case self.weapon_skill_input_box:
                if attack_data.weapon_skill >= 6:
                    attack_data.weapon_skill == 6
                else: attack_data.weapon_skill += 1
                
            # case self.attack_modifier_input:
            #     attack_data.attack_modifier += 1
            
        
    def click_decrement_button(self, decrement_area, instance): #decrement button action and conditionals
        match decrement_area :
            case self.attacks_input_box:
                if attack_data.attacks_number <= 1:
                    attack_data.attacks_number = 1
                    return
                attack_data.attacks_number -= 1
                
            case self.units_input_box:
                if attack_data.units_number <= 1:
                    attack_data.units_number = 1
                    return
                attack_data.units_number -= 1

            case self.weapon_skill_input_box:
                if attack_data.weapon_skill <= 1:
                    attack_data.weapon_skill = 1
                    return
                attack_data.weapon_skill -= 1
            
        
        
    
    
    

if __name__ == "__main__":
    DiceRollerApp().run()