algsGroups = {
    "All Edges Oriented Correctly" : [26, 27, 21, 22, 24, 25, 23],
    "T-Shapes" : [33, 45],
    "Squares" : [5, 6],
    "C-Shapes" : [34, 46],
    "W-Shapes" : [36, 38],
    "Corners Correct, Edges Flipped" : [28, 57],
    "P-Shapes" : [31, 32, 43, 44],
    "I-Shapes" : [51, 56, 52, 55],
    "Fish-Shapes" : [9, 10, 35, 37],
    "Knight Move Shapes" : [13, 14, 15, 16],
    "Awkward Shapes" : [29, 30, 41, 42],
    "L-Shapes" : [48, 47, 49, 50, 53, 54],
    "Lightning Bolts" : [7, 8, 11, 12, 39, 40],
    "No Edges Flipped Correctly" : [1,2,3,4,18,19,17,20],
};

algsInfo = {
    1: {
        "name": "Runway",
        "a": "(R U2') (R2' F R F') U2' (R' F R F')",
        "a2": "",
    },
    2: {
        "name": "Zamboni",
        "a": "(R U' R2 D') r U r' (D R2 U R')",
        "a2": "",
    },
    3: {
        "name": "Anti-Mouse",
        "a": "(R' F2 R2 U2 R') F (R U2 R2 F2 R)",
        "a2": "",
    },
    4: {
        "name": "Mouse",
        "a": "(R' F2 R2 U2 R') F' (R U2 R2 F2 R)",
        "a2": "",
    },
    5: {
        "name": "Lefty Square",
        "a": "(r' U2' R U R' U r)",
        "a2": "",
    },
    6: {
        "name": "Righty Square",
        "a": "(r U2 R' U' R U' r')",
        "a2": "",
    },
    7: {
        "name": "Fat Sune",
        "a": "(r U R' U R U2' r')",
        "a2": "",
    },
    8: {
        "name": "Fat Antisune",
        "a": "(r' U' R U' R' U2 r)",
        "a2": "",
    },
    9: {
        "name": "Kite",
        "a": "(R U R' U') R' F (R2 U R' U') F'",
        "a2": "",
    },
    10: {
        "name": "Anti-Kite",
        "a": "(R U R' U) (R' F R F') (R U2' R')",
        "a2": "",
    },
    11: {
        "name": "Downstairs",
        "a": "r' (R2 U R' U R U2 R') U M'",
        "a2": "",
    },
    12: {
        "name": "Upstairs",
        "a": "M' (R' U' R U' R' U2 R) U' M",
        "a2": "",
    },
    13: {
        "name": "Gun",
        "a": "F U R U' R2' F' R U (R U' R')",
        "a2": "",
    },
    14: {
        "name": "Anti-Gun",
        "a": "(R' F R) (U R' F' R) (F U' F')",
        "a2": "",
    },
    15: {
        "name": "Squeegee",
        "a": "(r' U' r) (R' U' R U) (r' U r)",
        "a2": "",
    },
    16: {
        "name": "Anti-Squeegee",
        "a": "(r U r') (R U R' U') (r U' r')",
        "a2": "",
    },
    17: {
        "name": "Slash",
        "a": "(F R' F' R) U S' (R U' R') S ",
        "a2": "",
    },
    18: {
        "name": "Crown",
        "a": "(F S') (R U' R' S) (R U2 R') (U' F')",
        "a2": "",
    },
    19: {
        "name": "Bunny",
        "a": "S' R U R' S U' (R' F R F')",
        "a2": "",
    },
    20: {
        "name": "Checkers",
        "a": "(r U R' U') M2' (U R U' R') U' M'",
        "a2": "",
    },
    21: {
        "name": "Double Headlights",
        "a": "(R U R' U) (R U' R' U) (R U2' R')",
        "a2": "",
    },
    22: {
        "name": "Pi-Shape",
        "a": "R U2 R2 U' R2 U' R2 U2 R",
        "a2": "",
    },
    23: {
        "name": "U-Shape",
        "a": "R2 D (R' U2 R) D' (R' U2 R')",
        "a2": "",
    },
    24: {
        "name": "Hammerhead",
        "a": "(r U R' U') (r' F R F')",
        "a2": "",
    },
    25: {
        "name": "L-Shape",
        "a": "F' (r U R' U') r' F R",
        "a2": "",
    },
    26: {
        "name": "Antisune",
        "a": "(R U2 R') (U' R U' R')",
        "a2": "",
    },
    27: {
        "name": "Sune",
        "a": "(R U R' U) (R U2' R')",
        "a2": "",
    },
    28: {
        "name": "Stealth",
        "a": "S' (R U R') S (R U' R') ",
        "a2": "",
    },
    29: {
        "name": "Spotted Chameleon",
        "a": "r2 D' r U r' D r2 U' r' U' r",
        "a2": "",
    },
    30: {
        "name": "Anti-Spotted Chameleon",
        "a": "r' D' r U' r' D r2 U' r' U r U r'",
        "a2": "",
    },
    31: {
        "name": "Couch",
        "a": "(R' U' F) (U R U' R') F' R",
        "a2": "",
    },
    32: {
        "name": "Anti-Couch",
        "a": "S (R U R' U') (R' F R f')",
        "a2": "",
    },
    33: {
        "name": "Key",
        "a": "(R U R' U') (R' F R F')",
        "a2": "",
    },
    34: {
        "name": "City",
        "a": "(f R f') (U' r' U' R) (U M')",
        "a2": "",
    },
    35: {
        "name": "Fish Salad",
        "a": "(R U2') (R2' F R F') (R U2' R')",
        "a2": "",
    },
    36: {
        "name": "Sea Mew",
        "a": "(R U R' F') (R U R' U') (R' F R U') (R' F R F')",
        "a2": "",
    },
    37: {
        "name": "Mounted Fish",
        "a": "(F R' F' R) (U R U' R')",
        "a2": "",
    },
    38: {
        "name": "Mario",
        "a": "(R U R' U) (R U' R' U') (R' F R F')",
        "a2": "",
    },
    39: {
        "name": "Fung",
        "a": "f' (r U r' U') (r' F r S)",
        "a2": "",
    },
    40: {
        "name": "Anti-Fung",
        "a": "(f R' F' R) (U R U' R') S'",
        "a2": "",
    },
    41: {
        "name": "Awkward Fish",
        "a": "(R U R' U R U2' R') F (R U R' U') F'",
        "a2": "",
    },
    42: {
        "name": "Anti-Awkward Fish",
        "a": "(F S') (R U R' U') (F' U S)",
        "a2": "",
    },
    43: {
        "name": "Anti-P",
        "a": "y R' U' F' U F R",
        "a2": "",
    },
    44: {
        "name": "P-Shape",
        "a": "F (U R U' R') F'",
        "a2": "",
    },
    45: {
        "name": "T-Shape",
        "a": "F (R U R' U') F'",
        "a2": "",
    },
    46: {
        "name": "Seein' Headlights",
        "a": "R' U' (R' F R F') U R",
        "a2": "",
    },
    47: {
        "name": "Anti-Breakneck",
        "a": "(F R' F' R) U2 (R U' R' U) (R U2 R')",
        "a2": "",
    },
    48: {
        "name": "Breakneck",
        "a": "F (R U R' U') (R U R' U') F'",
        "a2": "",
    },
    49: {
        "name": "Right back squeezy",
        "a": "r U' (r2 U) (r2 U) (r2) U' r",
        "a2": "",
    },
    50: {
        "name": "Right front squeezy",
        "a": "r' U r2 U' r2' U' r2 U r'",
        "a2": "",
    },
    51: {
        "name": "Bottlecap",
        "a": "F (U R U' R') (U R U' R') F'",
        "a2": "",
    },
    52: {
        "name": "Rice Cooker",
        "a": "R' (F' U' F U') (R U R' U) R",
        "a2": "",
    },
    53: {
        "name": "Frying Pan",
        "a": "(r' U' R U') (R' U R U') (R' U2 r)",
        "a2": "",
    },
    54: {
        "name": "Anti-Frying Pan",
        "a": "(r U R' U) (R U' R' U) R U2' r'",
        "a2": "",
    },
    55: {
        "name": "Highway",
        "a": "y (R' F R U) (R U' R2' F') R2 U' R' (U R U R')",
        "a2": "",
    },
    56: {
        "name": "Streetlights",
        "a": "(r U r') (U R U' R') (U R U' R') (r U' r')",
        "a2": "",
    },
    57: {
        "name": "H-Shape",
        "a": "(R U' R' S') (R U R' S)",
        "a2": "",
    },
};

def standard_to_latex(alg: str) -> str:
    latex_moves = alg
    latex_moves = latex_moves.replace("(", "")
    latex_moves = latex_moves.replace(")", "")
    latex_moves = latex_moves.replace("2'", "2")
    latex_moves = latex_moves.replace("'", "p")
    latex_moves = latex_moves.replace("r", "Rw")
    latex_moves = latex_moves.replace("l", "Lw")
    latex_moves = latex_moves.replace("u", "Uw")
    latex_moves = latex_moves.replace("d", "Dw")
    latex_moves = latex_moves.replace("f", "Fw")
    latex_moves = latex_moves.replace("b", "Bw")
    latex_moves = latex_moves.replace(" ", ", ")
    return latex_moves

def alg_to_standard(alg: str) -> str:
    std = alg
    std = std.replace("(", "")
    std = std.replace(")", "")
    return std
## my original code:
#def inverse(alg: str) -> str:
#    moves = alg.split()
#    moves = moves[::-1]
#    inverted = []
#    for i, move in enumerate(moves):
#        if len(move) == 2 and move[1] == "'":
#            inverted.append(move[0])
#        elif len(move) == 2 and move[1] == "2":
#            inverted.append(move)
#        else:
#            if len(move) == 3:
#                inverted.append(move)
#            else:
#                inverted.append(move + "'")
#
#    return ", ".join(inverted)

def inverse(alg: str) -> str:
    # Extract bracket structure and positions from original moves
    moves = alg.split()
    bracket_info = []  # Track which moves have brackets
    
    for i, move in enumerate(moves):
        has_open = '(' in move
        has_close = ')' in move
        bracket_info.append((has_open, has_close))
    
    # Extract moves without brackets
    moves_no_brackets = [move.replace('(', '').replace(')', '') for move in moves]
    
    # Reverse moves and bracket info
    moves_no_brackets = moves_no_brackets[::-1]
    bracket_info = bracket_info[::-1]
    
    # When reversed, opening and closing brackets swap positions
    bracket_info = [(close, open) for open, close in bracket_info]
    
    # Invert each move
    inverted = []
    for move in moves_no_brackets:
        if len(move) == 2 and move[1] == "'":
            inverted.append(move[0])
        elif len(move) == 2 and move[1] == "2":
            inverted.append(move)
        else:
            if len(move) == 3:
                inverted.append(move)
            else:
                inverted.append(move + "'")
    
    # Add brackets back in the same relative positions
    result = []
    for i, move in enumerate(inverted):
        has_open, has_close = bracket_info[i]
        if has_open:
            move = '(' + move
        if has_close:
            move = move + ')'
        result.append(move)
    
    return " ".join(result)

with open ("oll.csv", "w") as f:
    f.write(f"Group|OLL|Name|STM|Alg|Inverse|Std|Std Inv|Latex\n")
    for group in algsGroups:
        print(f"*{group}* :")
        for oll in algsGroups[group]:
            name = algsInfo[oll]['name']
            print(f"\"{name}\" (OLL {oll})", end = ", ")
            alg = algsInfo[oll]['a']
            latex = standard_to_latex(alg)
            inv = inverse(alg)
            std = alg_to_standard(alg)
            std_inv = alg_to_standard(inv)
            stm = len(std.split())
            f.write(f"{group}|{oll}|{name}|{stm}|{alg}|{inv}|{std}|{std_inv}|{latex}\n")
        print()
        print()
