# main.py

import matplotlib.pyplot as plt
import random
from moves_cube import *
from MagicCube.code import cube_interactive
from logic_cube import RubiksCube
from solver import IterativeDeepeningSearch, BreadthFirstSearch
from visual_utils import scramble_visual_cube, animate_solution_by_event

def generate_random_scramble(num_moves):
    available_moves = [
        "F", "F'", "F2", "R", "R'", "R2", "U", "U'", "U2",
        "B", "B'", "B2", "L", "L'", "L2", "D", "D'", "D2"
    ]
    return random.choices(available_moves, k=num_moves)

if __name__ == "__main__":
    SCRAMBLE_LENGTH = 4
    scramble_moves = generate_random_scramble(SCRAMBLE_LENGTH)
    
    all_move_functions = {
        "F": move_F, "F'": move_F_prime, "F2": move_F2,
        "R": move_R, "R'": move_R_prime, "R2": move_R2,
        "U": move_U, "U'": move_U_prime, "U2": move_U2,
        "B": move_B, "B'": move_B_prime, "B2": move_B2,
        "L": move_L, "L'": move_L_prime, "L2": move_L2,
        "D": move_D, "D'": move_D_prime, "D2": move_D2,
    }

    logical_cube = RubiksCube()
    for move_str in scramble_moves:
        move_func = all_move_functions[move_str]
        logical_cube = logical_cube.apply_move(move_func)

    
    # solver = IterativeDeepeningSearch(logical_cube)
    solver = BreadthFirstSearch(logical_cube)

    solution_moves = solver.solve()

    if solution_moves:
        
        visual_cube = cube_interactive.Cube(3)
        scramble_visual_cube(visual_cube, scramble_moves)
        visual_cube.draw_interactive()
        interactive_cube_instance = plt.gca()
        
        animate_solution_by_event(interactive_cube_instance, solution_moves)
        plt.show()
    else:
        print("Solution not found within the algorithm's limits.")