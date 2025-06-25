class RubiksCube:
    def __init__(self, state=None):
        if state is None:
            self.state = list('WWWWWWWWWBBBBBBBBBOOOOOOOOOGGGGGGGGGRRRRRRRRRYYYYYYYYY')
        else:
            self.state = list(state)

    def __str__(self):
        return "".join(self.state)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)

    def is_solved(self):
        for i in range(6):
            face_start_index = i * 9
            first_color = self.state[face_start_index]
            for j in range(1, 9):
                if self.state[face_start_index + j] != first_color:
                    return False
        return True

    def apply_move(self, move_func):
        new_state = self.state[:]
        move_func(new_state)
        return RubiksCube(new_state)
    
    