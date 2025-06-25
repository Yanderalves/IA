import matplotlib.pyplot as plt

class MockEvent:
    def __init__(self, key):
        self.key = key

def simulate_key_press(interactive_cube, key_char):
    event = MockEvent(key_char)
    interactive_cube._key_press(event)
    interactive_cube._key_release(event)

def animate_solution_by_event(interactive_cube, moves):
    animation_speed = 0.8
    plt.pause(1.0)
    for move in moves:
        face_key = move[0].lower()
        is_prime = (len(move) > 1 and move[1] == "'")
        is_double = (len(move) > 1 and move[1] == '2')
        if is_prime:
            shift_event = MockEvent('shift')
            face_event = MockEvent(face_key)
            interactive_cube._key_press(shift_event)
            interactive_cube._key_press(face_event)
            interactive_cube._key_release(face_event)
            interactive_cube._key_release(shift_event)
        elif is_double:
            simulate_key_press(interactive_cube, face_key)
            plt.pause(animation_speed)
            simulate_key_press(interactive_cube, face_key)
        else:
            simulate_key_press(interactive_cube, face_key)
        plt.pause(animation_speed)

def scramble_visual_cube(cube_object, moves):
    for move in moves:
        face = move[0].upper()
        turns = 1
        if len(move) > 1:
            if move[1] == "'":
                turns = -1
            elif move[1] == '2':
                cube_object.rotate_face(face, 1)
                turns = 1
        cube_object.rotate_face(face, turns)