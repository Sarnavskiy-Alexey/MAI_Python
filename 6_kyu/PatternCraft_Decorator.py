"""
    Reference: https://www.codewars.com//kata/5682e545fb263ecf7b000069
"""

class Marine:
    damage = 0
    armor = 0
    def __init__(self, damage, armor):
        self.damage = damage
        self.armor = armor


class Marine_weapon_upgrade:
    damage = 0
    armor = 0
    def __init__(self, marine):
        self.armor = marine.armor
        self.damage = marine.damage + 1


class Marine_armor_upgrade:
    damage = 0
    armor = 0
    def __init__(self, marine):
        self.armor = marine.armor + 1
        self.damage = marine.damage

if __name__ == '__main__':
    marine = Marine(10, 1)
    print(Marine_weapon_upgrade(marine).damage, '==', 11)
    print(marine.damage, '==', 10)

    marine = Marine_weapon_upgrade(marine)
    print(Marine_weapon_upgrade(marine).damage, '==', 12)

    marine = Marine(15, 10)
    marine = Marine_armor_upgrade(marine)
    marine = Marine_armor_upgrade(marine)
    print(marine.armor, '==', 12)