from random import randint

class Die:
    """A model of a die, with 6 sides as a default"""
    
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

def main():
    new_die = Die()
    print(f"\nRolling {new_die.sides}-sided die...")
    for _ in range(1, 11): 
        new_die.roll_die()
    
    new_die_2 = Die(10)
    print(f"\nRolling {new_die_2.sides}-sided die...")
    for _ in range(1, 11):
        new_die_2.roll_die()
        
    new_die_3 = Die(20)
    print(f"\nRolling {new_die_3.sides}-sided die...")
    for _ in range(1, 11):
        new_die_3.roll_die()

if __name__ == '__main__':
    main()
