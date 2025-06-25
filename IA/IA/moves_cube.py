def move_F(state):
    """Gira a face da Frente (Front) no sentido horário."""
    # Gira a própria face F
    state[18], state[19], state[20], state[21], state[23], state[24], state[25], state[26] = \
    state[24], state[21], state[18], state[25], state[19], state[26], state[23], state[20]
    # Move as peças das arestas adjacentes
    state[6], state[7], state[8], state[27], state[30], state[33], state[47], state[46], state[45], state[17], state[14], state[11] = \
    state[17], state[14], state[11], state[6], state[7], state[8], state[27], state[30], state[33], state[47], state[46], state[45]
    return state

def move_F_prime(state):
    """Gira a face da Frente (Front) no sentido anti-horário."""
    # Gira a própria face F
    state[18], state[19], state[20], state[21], state[23], state[24], state[25], state[26] = \
    state[20], state[23], state[26], state[19], state[25], state[18], state[21], state[24]
    # Move as peças das arestas adjacentes
    state[6], state[7], state[8], state[27], state[30], state[33], state[47], state[46], state[45], state[17], state[14], state[11] = \
    state[27], state[30], state[33], state[47], state[46], state[45], state[17], state[14], state[11], state[6], state[7], state[8]
    return state

def move_U(state):
    """Gira a face de Cima (Up) no sentido horário."""
    # Gira a própria face U
    state[0], state[1], state[2], state[3], state[5], state[6], state[7], state[8] = \
    state[6], state[3], state[0], state[7], state[1], state[8], state[5], state[2]
    # Move as arestas adjacentes
    state[18], state[19], state[20], state[27], state[28], state[29], state[36], state[37], state[38], state[9], state[10], state[11] = \
    state[27], state[28], state[29], state[36], state[37], state[38], state[9], state[10], state[11], state[18], state[19], state[20]
    return state

def move_U_prime(state):
    """Gira a face de Cima (Up) no sentido anti-horário."""
    # Gira a própria face U
    state[0], state[1], state[2], state[3], state[5], state[6], state[7], state[8] = \
    state[2], state[5], state[8], state[1], state[7], state[0], state[3], state[6]
    # Move as arestas adjacentes
    state[18], state[19], state[20], state[27], state[28], state[29], state[36], state[37], state[38], state[9], state[10], state[11] = \
    state[9], state[10], state[11], state[18], state[19], state[20], state[27], state[28], state[29], state[36], state[37], state[38]
    return state

def move_R(state):
    """Gira a face da Direita (Right) no sentido horário."""
    # Gira a própria face R
    state[27], state[28], state[29], state[30], state[32], state[33], state[34], state[35] = \
    state[33], state[30], state[27], state[34], state[28], state[35], state[32], state[29]
    # Move as arestas adjacentes
    state[8], state[5], state[2], state[26], state[23], state[20], state[53], state[50], state[47], state[36], state[39], state[42] = \
    state[26], state[23], state[20], state[53], state[50], state[47], state[36], state[39], state[42], state[8], state[5], state[2]
    return state

def move_R_prime(state):
    """Gira a face da Direita (Right) no sentido anti-horário."""
    # Gira a própria face R
    state[27], state[28], state[29], state[30], state[32], state[33], state[34], state[35] = \
    state[29], state[32], state[35], state[28], state[34], state[27], state[30], state[33]
    # Move as arestas adjacentes
    state[8], state[5], state[2], state[26], state[23], state[20], state[53], state[50], state[47], state[36], state[39], state[42] = \
    state[36], state[39], state[42], state[8], state[5], state[2], state[26], state[23], state[20], state[53], state[50], state[47]
    return state

def move_L(state):
    """Gira a face da Esquerda (Left) no sentido horário."""
    # Gira a própria face L
    state[9], state[10], state[11], state[12], state[14], state[15], state[16], state[17] = \
    state[15], state[12], state[9], state[16], state[10], state[17], state[14], state[11]
    # Move as arestas adjacentes
    state[0], state[3], state[6], state[44], state[41], state[38], state[45], state[48], state[51], state[18], state[21], state[24] = \
    state[44], state[41], state[38], state[45], state[48], state[51], state[18], state[21], state[24], state[0], state[3], state[6]
    return state
    
def move_L_prime(state):
    """Gira a face da Esquerda (Left) no sentido anti-horário."""
    # Gira a própria face L
    state[9], state[10], state[11], state[12], state[14], state[15], state[16], state[17] = \
    state[11], state[14], state[17], state[10], state[16], state[9], state[12], state[15]
    # Move as arestas adjacentes
    state[0], state[3], state[6], state[44], state[41], state[38], state[45], state[48], state[51], state[18], state[21], state[24] = \
    state[18], state[21], state[24], state[0], state[3], state[6], state[44], state[41], state[38], state[45], state[48], state[51]
    return state

def move_D(state):
    """Gira a face de Baixo (Down) no sentido horário."""
    # Gira a própria face D
    state[45], state[46], state[47], state[48], state[50], state[51], state[52], state[53] = \
    state[51], state[48], state[45], state[52], state[46], state[53], state[50], state[47]
    # Move as arestas adjacentes
    state[24], state[25], state[26], state[33], state[34], state[35], state[42], state[43], state[44], state[15], state[16], state[17] = \
    state[33], state[34], state[35], state[42], state[43], state[44], state[15], state[16], state[17], state[24], state[25], state[26]
    return state

def move_D_prime(state):
    """Gira a face de Baixo (Down) no sentido anti-horário."""
    # Gira a própria face D
    state[45], state[46], state[47], state[48], state[50], state[51], state[52], state[53] = \
    state[47], state[50], state[53], state[46], state[52], state[45], state[48], state[51]
    # Move as arestas adjacentes
    state[24], state[25], state[26], state[33], state[34], state[35], state[42], state[43], state[44], state[15], state[16], state[17] = \
    state[15], state[16], state[17], state[24], state[25], state[26], state[33], state[34], state[35], state[42], state[43], state[44]
    return state

def move_B(state):
    """Gira a face de Trás (Back) no sentido horário."""
    # Gira a própria face B
    state[36], state[37], state[38], state[39], state[41], state[42], state[43], state[44] = \
    state[42], state[39], state[36], state[43], state[37], state[44], state[41], state[38]
    # Move as arestas adjacentes
    state[2], state[1], state[0], state[35], state[32], state[29], state[51], state[52], state[53], state[9], state[12], state[15] = \
    state[35], state[32], state[29], state[51], state[52], state[53], state[9], state[12], state[15], state[2], state[1], state[0]
    return state

def move_B_prime(state):
    """Gira a face de Trás (Back) no sentido anti-horário."""
    # Gira a própria face B
    state[36], state[37], state[38], state[39], state[41], state[42], state[43], state[44] = \
    state[38], state[41], state[44], state[37], state[43], state[36], state[39], state[42]
    # Move as arestas adjacentes
    state[2], state[1], state[0], state[35], state[32], state[29], state[51], state[52], state[53], state[9], state[12], state[15] = \
    state[9], state[12], state[15], state[2], state[1], state[0], state[35], state[32], state[29], state[51], state[52], state[53]
    return state

def move_F2(state):
    return move_F(move_F(state))

def move_R2(state):
    return move_R(move_R(state))

def move_U2(state):
    return move_U(move_U(state))

def move_B2(state):
    return move_B(move_B(state))

def move_L2(state):
    return move_L(move_L(state))

def move_D2(state):
    return move_D(move_D(state))