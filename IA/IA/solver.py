from moves_cube import *
from logic_cube import RubiksCube
from collections import deque
import heapq


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
    

class AStarSearch:
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
        self.expanded_nodes_count = 0
        self.max_priority_queue_size = 0
        self._counter = 0 

    def _heuristic(self, cube_state):
        solved_state = list('WWWWWWWWWBBBBBBBBBOOOOOOOOOGGGGGGGGGRRRRRRRRRYYYYYYYYY')
        misplaced_tiles = 0
        for i in range(len(cube_state.state)):
            if cube_state.state[i] != solved_state[i]:
                misplaced_tiles += 1
        return misplaced_tiles

    def solve(self):
        self.priority_queue = [] 
        self.visited = {str(self.initial_cube): 0} 
        
        self.expanded_nodes_count = 0 
        self.max_priority_queue_size = 0
        self._counter = 0 
        
        g_cost = 0 
        h_cost = self._heuristic(self.initial_cube) 
        f_cost = g_cost + h_cost 
        
        heapq.heappush(self.priority_queue, (f_cost, g_cost, self._counter, [], self.initial_cube))
        self.max_priority_queue_size = max(self.max_priority_queue_size, len(self.priority_queue))
        self._counter += 1 
        
        while self.priority_queue:
            self.max_priority_queue_size = max(self.max_priority_queue_size, len(self.priority_queue)) 
            
            f_cost, g_cost, _, path, current_cube = heapq.heappop(self.priority_queue) 
            self.expanded_nodes_count += 1 

            if current_cube.is_solved():
                return path

            if g_cost > self.visited.get(str(current_cube), float('inf')):
                continue

            for move_name, move_func in self.moves.items():
                new_cube = current_cube.apply_move(move_func)
                new_g_cost = g_cost + 1 
                
                if str(new_cube) not in self.visited or new_g_cost < self.visited[str(new_cube)]:
                    self.visited[str(new_cube)] = new_g_cost 
                    new_h_cost = self._heuristic(new_cube) 
                    new_f_cost = new_g_cost + new_h_cost 
                    
                    heapq.heappush(self.priority_queue, (new_f_cost, new_g_cost, self._counter, path + [move_name], new_cube))
                    self._counter += 1 
        
        return None