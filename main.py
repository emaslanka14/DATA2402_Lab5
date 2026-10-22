from characters import Character, Fighter, Mage
from weapons import Weapon, MeleeWeapon, RangedWeapon, MagicWeapon

def attack(attacker: Character, weapon: Weapon, target: Character, distance: int) -> None:
    
    # only Mages can use a MagicWeapon
    if isinstance(weapon, MagicWeapon) and not isinstance(attacker, Mage):
        raise TypeError("Only Mages can use a Magic Weapon")

    if isinstance(weapon, (RangedWeapon, MagicWeapon)):
        # can't exceed the weapon's range
        if distance > weapon.range:
            raise ValueError(f"Target is out of range by {distance - weapon.range}")
    if isinstance(weapon, MeleeWeapon):
        # weapons without a range only work at distance 0
        if distance > 0:
            raise ValueError("This weapon has no range and can't be used at a distance")

    target.health -= weapon.damage
    print(f"{target.name} was struck for {weapon.damage} damage by {attacker.name}")

