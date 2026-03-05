import random

def initialise_grid():

    """Create a 5x5 grid filled with '-'."""

    return[['-' for _ in range(5)] _ in range(5)] 


def place_treasure():

    """Randomly choose treasures row and columns"""

    return random.randint(0,4),random.randint(0,4)



def give_hint(treasure_row, treasure_col, guess_row, guess_column):

    """provide a directional hint based on the player's guess"""

    if guess_row < treasure_row:

        return "Move down"
    
    elif guess_row > treasure_row:

        return "Move up"
    
    

    elif guess_column < treasure_col:

        return "move right"
    

    elif guess_column > treasure_col:

        return "move left"
    
    return "Congradulations, you found the treasure"

def treasure_hunt():

    grid = initialise_grid()

    treasure_row, treasure_column = _place_treasure()

