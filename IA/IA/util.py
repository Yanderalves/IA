import random

def generate_random_scramble(num_moves):
    available_moves = [
        "F", "F'", "F2", "R", "R'", "R2", "U", "U'", "U2",
        "B", "B'", "B2", "L", "L'", "L2", "D", "D'", "D2"
    ]
    return random.choices(available_moves, k=num_moves)
