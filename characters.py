from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name: str, health: int):
        # Shared attributes for all characters
        self.name = name
        self.health = health

    @abstractmethod
    def save(self, filename: str) -> None:
        # Must be implemented by all subclasses
        pass

    @abstractmethod
    def __repr__(self) -> str:
        # Must be implemented by all subclasses
        pass


class Fighter(Character):
    def __init__(self, name: str, health: int, speed: int):
        # Initialize shared attributes using parent constructor
        super().__init__(name, health)
        # Fighter-specific attribute
        self.speed = speed

    def save(self, filename: str) -> None:
        # Save Fighter-specific data
        pass

    def __repr__(self) -> str:
        # Return a readable string representation of a Fighter object
        return f"Fighter(name={self.name}, health={self.health}, speed={self.speed})"


class Mage(Character):
    def __init__(self, name: str, health: int, mana: int):
        # Initialize shared attributes using parent constructor
        super().__init__(name, health)
        # Mage-specific attribute
        self.mana = mana

    def save(self, filename: str) -> None:
        # Save Mage-specific data
        pass

    def __repr__(self) -> str:
        # Return a readable string representation of a Mage object
        return f"Mage(name={self.name}, health={self.health}, mana={self.mana})"