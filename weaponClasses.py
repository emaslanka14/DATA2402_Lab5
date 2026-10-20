from abc import ABC, abstractmethod

class Weapon(ABC):

    def __init__(self, name:str, damage:float):
        self.name = name
        self.damage = damage

    def save(self, filename)->None:
        with open(filename, "w") as f:
            f.write(str(self))
    
    @abstractmethod
    def __repr__(self):
        pass

    def __str__(self):
        return f"Weapon {self.name} with {self.damage} damage."

        
class MeleeWeapon(Weapon):
    def __repr__(self):
        return f"Melee Weapon {self.name} with {self.damage} damage."

class RangedWeapon(Weapon):

    def __init__(self, name:str, damage:float, range:float):
        super().__init__(name, damage)
        self.range = range

    def __repr__(self):
        return f"Ranged Weapon {self.name} with {self.damage} damage and {self.range} range."

class MagicWeapon(Weapon):

    def __init__(self, name:str, damage:float, range:float, manaCost:float):
        super().__init__(name, damage)
        self.range = range
        self.manaCost = manaCost


    def __repr__(self):
        return f"Magic Weapon {self.name} with {self.damage} damage and {self.range} range. Has a mana cost of {self.manaCost}."
