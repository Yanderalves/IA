import matplotlib.pyplot as plt
import random
import time
from moves_cube import *
from MagicCube.code import cube_interactive
from logic_cube import RubiksCube
from solver import IterativeDeepeningSearch, BreadthFirstSearch, AStarSearch
from visual_utils import scramble_visual_cube, animate_solution_by_event

def solutions():
    mapa_solvers = {
        '1': BreadthFirstSearch,
        '2': IterativeDeepeningSearch,
        '3': AStarSearch
    }
    
    while True:
        print("\nEscolha o algoritmo para solucionar o cubo:")
        print("  1: Busca em Largura (BFS)")
        print("  2: Busca em Profundidade Iterativa (IDFS)")
        print("  3: Busca A*")
        escolha = input("Digite o número (1, 2 ou 3): ")
        
        if escolha in mapa_solvers:
            solver_class = mapa_solvers[escolha]
            break
        else:
            print("Opção inválida. Tente novamente.")

    while True:
        try:
            num_str = input("\nQuantos movimentos aleatórios para embaralhar? ")
            num_movimentos = int(num_str)
            if num_movimentos > 0:
                break
            else:
                print("Por favor, digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            
    return solver_class, num_movimentos

def generate_random_scramble(num_moves):
    available_moves = [
        "F", "F'", "F2", "R", "R'", "R2", "U", "U'", "U2",
        "B", "B'", "B2", "L", "L'", "L2", "D", "D'", "D2"
    ]
    return random.choices(available_moves, k=num_moves)

if __name__ == "__main__":
    solver_class, scramble_length = solutions()
    
    scramble_moves = generate_random_scramble(scramble_length)
    print(f"\nEmbaralhamento gerado: {' '.join(scramble_moves)}")
    print("Iniciando busca pela solução... ")
    
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

    solver = solver_class(logical_cube)
    
    start_time = time.time()
    solution_moves = solver.solve()
    end_time = time.time()
    
    execution_time = end_time - start_time

    if solution_moves:
        print(f"Solução encontrada em {execution_time:.4f} segundos!!")
        
        visual_cube = cube_interactive.Cube(3)
        scramble_visual_cube(visual_cube, scramble_moves)
        visual_cube.draw_interactive()
        interactive_cube_instance = plt.gca()
        
        animate_solution_by_event(interactive_cube_instance, solution_moves)
        plt.show()
    else:
        print(f"Solução não encontrada dentro dos limites do algoritmo (tempo de busca: {execution_time:.4f} segundos).")