from moves_cube import *
from logic_cube import RubiksCube
from collections import deque


class BreadthFirstSearch:
    def __init__(self, initial_cube):
        self.initial_cube = initial_cube
        self.moves = IterativeDeepeningSearch(initial_cube).moves

    def solve(self):
        queue = deque([(self.initial_cube, [])])
        visited = {str(self.initial_cube)}

        while queue:
            current_cube, path = queue.popleft()

            if current_cube.is_solved():
                return path

            for move_name, move_func in self.moves.items():
                new_cube = current_cube.apply_move(move_func)
                if str(new_cube) not in visited:
                    visited.add(str(new_cube))
                    new_path = path + [move_name]
                    queue.append((new_cube, new_path))
        
        return None

class IterativeDeepeningSearch:
    def __init__(self, initial_cube):
        self.initial_cube = initial_cube
        self.moves = {
            "F": move_F, "F'": move_F_prime, "F2": move_F2,
            "R": move_R, "R'": move_R_prime, "R2": move_R2,
            "U": move_U, "U'": move_U_prime, "U2": move_U2,
            "B": move_B, "B'": move_B_prime, "B2": move_B2,
            "L": move_L, "L'": move_L_prime, "L2": move_L2,
            "D": move_D, "D'": move_D_prime, "D2": move_D2,
        }

    def solve(self):
        max_depth_limit = 10
        for depth in range(max_depth_limit):
            print(f"Buscando com profundidade máxima: {depth}")
            visited_in_path = {str(self.initial_cube)}
            result = self._dls(self.initial_cube, depth, [], visited_in_path)
            if result is not None:
                return result
        return None

    def _dls(self, cube, limit, path, visited_in_path):
        if cube.is_solved():
            return path
        if limit <= 0:
            return None
        
        for move_name, move_func in self.moves.items():
            new_cube = cube.apply_move(move_func)
            if str(new_cube) not in visited_in_path:
                visited_in_path.add(str(new_cube))
                result = self._dls(new_cube, limit - 1, path + [move_name], visited_in_path)
                if result is not None:
                    return result
                visited_in_path.remove(str(new_cube))
        return None