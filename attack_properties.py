from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout

#Stats related to attack rolls:
class AttackProperties(BoxLayout):    
    weapon_skill = NumericProperty(3)  #WS
    attacks_number = NumericProperty(1)  #A
    units_number = NumericProperty(1) #number of units attacking    
    attacks_number_modifier = NumericProperty(0) #To implement later ?  
    # Rapid fire x = x extra attack if unit under 12"
    # Sustained Hits x = on 6 roll x extra attack rolls
    