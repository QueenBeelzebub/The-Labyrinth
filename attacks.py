from items import *
from random import randint

def roll(dice_sides, dice):
    """
    :param dice_sides: The sides on the dice you wish to roll, e.g. 20 for D20, 6 for D6
    :param dice: The amount of dice that will be rolled
    """
    value = 0
    for i in range(dice):
        value += randint(1, dice_sides)
    return value

def roll_check(min_value, crit):
    """
    Returns a number for a check on a D20, 
    :param min_value: The minimum value required to pass the check
    :param crit: The minimum value to crit, which doubles dice rolled
    """
    number = randint(1, 20)
    if number >= crit:
        return 2
    elif number >= min_value:
        return 1
    return 0


class Attack:
    def __init__(self, hit_roll, hit_dice, amount_of_dice, crit_roll) -> None:
        """
        :param hit_roll: Min number on a D20 to hit
        :param hit_dice: If hit, what dice is used to calculate damage
        :param amount_of_dice: If hit, how many dice are used to calculate damage
        :param crit_roll: what roll is required to crit
        """
        self.hit_roll = hit_roll
        self.hit_dice = hit_dice
        self.amount_of_dice = amount_of_dice
        self.crit_roll = crit_roll

    def roll_to_hit(self):
        return roll_check(self.hit_roll, self.crit_roll)
    
    def attack(self):
        damage = 0
        damage += roll(self.hit_dice, self.amount_of_dice*self.roll_to_hit())
        return damage
        pass

punch = Attack(15, 4, 1, 20)

bite = Attack(10, 6, 2, 20)