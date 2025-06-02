from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout

#Stats related to attack rolls:
class AttackProperties(BoxLayout):    
    weapon_skill = NumericProperty(3)  #WS
    attacks_number = NumericProperty(1)  #A
    units_attacking = NumericProperty(1) #number of units attacking    
    attack_modifier = NumericProperty(0)