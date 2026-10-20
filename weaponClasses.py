from abc import ABC, abstractmethod

class Weapon(ABC):

    def __init__(self, name:str, damage:float):
        self.name
        self.damage

    def save(self, filename)->None:
        with open(filename, "w") as f:
            f.write(str(self))
    
    @abstractmethod
    def __repr__(self):
        pass

    def __str__(self):
        return f"Weapon {self.name} with {self.damage} damage."

        


class MeleeWeapon(Weapon):
    pass

class RangedWeapon(Weapon):

    def __init__(self, name:str, damage:float, range:float):
        super().__init__(name, damage)
        self.range = range

    def save(self, filename):
        pass

class MagicWeapon(Weapon):

    def __init__(self, name:str, damage:float, range:float, manaCost:float):
        super().__init__(name, damage)
        self.range = range
        self.manaCost = manaCost


    def save(self, filename):
        pass

    def __repr__(self):
        return f"MagicWeapon"
