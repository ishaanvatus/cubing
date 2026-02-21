import collections
import csv, json
import shutil, os
groups = {
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
olls =  {
  26: {
    "name": "Antisune",
    "alg": "(R U2 R') (U' R U' R')",
    "gen": "27",
    "setup": "27"
  },
  21: {
    "name": "Double Headlights",
    "alg": "(R U R' U) (R U' R' U) (R U2' R')",
    "gen": "21",
    "setup": "U | Z-perm"
  },
  24: {
    "name": "Hammerhead",
    "alg": "(r U R' U') (r' F R F')",
    "gen": "25",
    "setup": "U | 25 | Ab-perm | U'"
  },
  25: {
    "name": "L-Shape",
    "alg": "F' (r U R' U') r' F R",
    "gen": "24",
    "setup": "U2 | 25 | U | E-perm | U"
  },
  22: {
    "name": "Pi-Shape",
    "alg": "R U2 R2 U' R2 U' R2 U2 R",
    "gen": "22",
    "setup": "21 | U' | Ua-perm | U"
  },
  27: {
    "name": "Sune",
    "alg": "(R U R' U) (R U2' R')",
    "gen": "26",
    "setup": "26"
  },
  23: {
    "name": "U-Shape",
    "alg": "R2 D (R' U2 R) D' (R' U2 R')",
    "gen": "25",
    "setup": "U | 25 | U' | E-perm"
  },
  42: {
    "name": "Anti-Awkward Fish",
    "alg": "(F S') (R U R' U') (F' U S)",
    "gen": "31",
    "setup": "U' | 31 | Ua-perm"
  },
  30: {
    "name": "Anti-Spotted Chameleon",
    "alg": "r' D' r U' r' D r2 U' r' U r U r'",
    "gen": "33",
    "setup": "U2 | 33 | U2 | Jb-perm | U2"
  },
  41: {
    "name": "Awkward Fish",
    "alg": "(R U R' U R U2' R') F (R U R' U') F'",
    "gen": "43",
    "setup": "43 | U' | Ua-perm | U"
  },
  29: {
    "name": "Spotted Chameleon",
    "alg": "r2 D' r U r' D r2 U' r' U' r",
    "gen": "33",
    "setup": "U2 | 33 | Aa-perm | U'"
  },
  34: {
    "name": "City",
    "alg": "(f R f') (U' r' U' R) (U M')",
    "gen": "37",
    "setup": "U | 37 | U | Aa-perm | U2"
  },
  46: {
    "name": "Seein' Headlights",
    "alg": "R' U' (R' F R F') U R",
    "gen": "43",
    "setup": "U' | 43 | U\u2019 | Z-perm | U\u2019"
  },
  57: {
    "name": "H-Shape",
    "alg": "(R U' R' S') (R U R' S)",
    "gen": "28",
    "setup": "28"
  },
  28: {
    "name": "Stealth",
    "alg": "S' (R U R') S (R U' R') ",
    "gen": "57",
    "setup": "57"
  },
  10: {
    "name": "Anti-Kite",
    "alg": "(R U R' U) (R' F R F') (R U2' R')",
    "gen": "8",
    "setup": "8 | U2 | Y-perm | U'"
  },
  35: {
    "name": "Fish Salad",
    "alg": "(R U2') (R2' F R F') (R U2' R')",
    "gen": "37",
    "setup": "U | 37 | U | Ra-perm | U2"
  },
  9: {
    "name": "Kite",
    "alg": "(R U R' U') R' F (R2 U R' U') F'",
    "gen": "13",
    "setup": "13"
  },
  37: {
    "name": "Mounted Fish",
    "alg": "(F R' F' R) (U R U' R')",
    "gen": "33",
    "setup": "33"
  },
  51: {
    "name": "Bottlecap",
    "alg": "F (U R U' R') (U R U' R') F'",
    "gen": "48",
    "setup": "48"
  },
  55: {
    "name": "Highway",
    "alg": " (R' F U R U') (R2 F' R2) (U R' U' R)",
    "gen": "50",
    "setup": "U2 | 50 | Jb-perm"
  },
  52: {
    "name": "Rice Cooker",
    "alg": "R' (F' U' F U') (R U R' U) R",
    "gen": "52",
    "setup": "U2 | 52 | U2"
  },
  56: {
    "name": "Streetlights",
    "alg": "(r U r') (U R U' R') (U R U' R') (r U' r')",
    "gen": "54",
    "setup": "U | 54 | Ua-perm | U'"
  },
  14: {
    "name": "Anti-Gun",
    "alg": "(R' F R) (U R' F' R) (F U' F')",
    "gen": "10",
    "setup": "U' | 10 | Jb-perm | U"
  },
  16: {
    "name": "Anti-Squeegee",
    "alg": "(r U r') (R U R' U') (r U' r')",
    "gen": "7",
    "setup": "7 | U2 | Ub-perm | U2"
  },
  13: {
    "name": "Gun",
    "alg": "F U R U' R2' F' R U (R U' R')",
    "gen": "9",
    "setup": "9"
  },
  15: {
    "name": "Squeegee",
    "alg": "(r' U' r) (R' U' R U) (r' U r)",
    "gen": "8",
    "setup": "8 | Ua-perm"
  },
  47: {
    "name": "Anti-Breakneck",
    "alg": "(F R' F' R) U2 (R U' R' U) (R U2 R')",
    "gen": "48",
    "setup": "48 | U' | Gb-perm"
  },
  54: {
    "name": "Anti-Frying Pan",
    "alg": "(r U R' U) (R U' R' U) R U2' r'",
    "gen": "54",
    "setup": "U | 54 | H-perm | U'"
  },
  48: {
    "name": "Breakneck",
    "alg": "F (R U R' U') (R U R' U') F'",
    "gen": "51",
    "setup": "51"
  },
  53: {
    "name": "Frying Pan",
    "alg": "(r' U' R U') (R' U R U') (R' U2 r)",
    "gen": "53",
    "setup": "U' | 53 | H-perm | U"
  },
  49: {
    "name": "Right back squeezy",
    "alg": "r U' (r2 U) (r2 U) (r2) U' r",
    "gen": "50",
    "setup": "50"
  },
  50: {
    "name": "Right front squeezy",
    "alg": "r' U r2 U' r2' U' r2 U r'",
    "gen": "49",
    "setup": "49"
  },
  40: {
    "name": "Anti-Fung",
    "alg": "(f R' F' R) (U R U' R') S'",
    "gen": "32",
    "setup": "32"
  },
  11: {
    "name": "Downstairs",
    "alg": "r' (R2 U R' U R U2 R') U M'",
    "gen": "7",
    "setup": "U' | 7 | U | Z-perm"
  },
  8: {
    "name": "Fat Antisune",
    "alg": "(r' U' R U' R' U2 r)",
    "gen": "5",
    "setup": "5"
  },
  7: {
    "name": "Fat Sune",
    "alg": "(r U R' U R U2' r')",
    "gen": "6",
    "setup": "6"
  },
  39: {
    "name": "Fung",
    "alg": "f' (r U r' U') (r' F r S)",
    "gen": "43",
    "setup": "U2 | 43 | U' | Z-perm | U"
  },
  12: {
    "name": "Upstairs",
    "alg": "M' (R' U' R U' R' U2 R) U' M",
    "gen": "8",
    "setup": "U | 8 | Z-perm | U"
  },
  3: {
    "name": "Anti-Mouse",
    "alg": "(R' F2 R2 U2 R') F (R U2 R2 F2 R)",
    "gen": "4",
    "setup": "4"
  },
  19: {
    "name": "Bunny",
    "alg": "S' R U R' S U' (R' F R F')",
    "gen": "17",
    "setup": "17"
  },
  20: {
    "name": "Checkers",
    "alg": "(S' R U R' S) U' (M' U R U' r')",
    "gen": "20",
    "setup": "20"
  },
  18: {
    "name": "Crown",
    "alg": "(F S') (R U' R' S) (R U2 R') (U' F')",
    "gen": "18",
    "setup": "U2 | 18 | U | Ub-perm | U"
  },
  4: {
    "name": "Mouse",
    "alg": "(R' F2 R2 U2 R') F' (R U2 R2 F2 R)",
    "gen": "3",
    "setup": "3"
  },
  1: {
    "name": "Runway",
    "alg": "(R U2') (R2' F R F') U2' (R' F R F')",
    "gen": "2",
    "setup": "U | 2 | V-perm | U"
  },
  17: {
    "name": "Slash",
    "alg": "(F R' F' R) U S' (R U' R') S ",
    "gen": "19",
    "setup": "19"
  },
  2: {
    "name": "Zamboni",
    "alg": "(R U' R2 D') r U r' (D R2 U R')",
    "gen": "1",
    "setup": "U | 1 | U' | Ja-perm | U2"
  },
  32: {
    "name": "Anti-Couch",
    "alg": "S (R U R' U') (R' F R f')",
    "gen": "40",
    "setup": "40"
  },
  43: {
    "name": "Anti-P",
    "alg": "R' U' F' U F R",
    "gen": "45",
    "setup": "U' | 45 | U | Ua-perm"
  },
  31: {
    "name": "Couch",
    "alg": "(R' U' F) (U R U' R') F' R",
    "gen": "40",
    "setup": "U2 | 40 | U | Ab-perm | U2"
  },
  44: {
    "name": "P-Shape",
    "alg": "F (U R U' R') F'",
    "gen": "45",
    "setup": "45"
  },
  5: {
    "name": "Lefty Square",
    "alg": "(r' U2' R U R' U r)",
    "gen": "8",
    "setup": "8"
  },
  6: {
    "name": "Righty Square",
    "alg": "(r U2 R' U' R U' r')",
    "gen": "7",
    "setup": "7"
  },
  33: {
    "name": "Key",
    "alg": "(R U R' U') (R' F R F')",
    "gen": "37",
    "setup": "37"
  },
  45: {
    "name": "T-Shape",
    "alg": "F (R U R' U') F'",
    "gen": "44",
    "setup": "44"
  },
  38: {
    "name": "Mario",
    "alg": "(R U R' U) (R U' R' U') (R' F R F')",
    "gen": "43",
    "setup": "U | 43 | U2 | Y-perm | U'"
  },
  36: {
    "name": "Sea Mew",
    "alg": "(R' F' U') F2 (U R U' R') (F' R)",
    "gen": "31",
    "setup": "U2 | 31 | U2 | Ua-perm | U2"
  }
}

repeat = 24
sanitize_filename = lambda string : string.replace(" ", "_").replace(",", "").lower()
f = open("curl.sh", "w")
for group in groups:
    print(f"*{group}*")
    path = sanitize_filename(group)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    for oll in groups[group]:
        name = olls[oll]["name"]
        name = sanitize_filename(name)
        name = name.replace("'", "")
        alg = olls[oll]["alg"]
        alg = alg.replace(")", "")
        alg = alg.replace("(", "")
        alg = alg.replace(" ", "")
        oll_path = "orders/" + sanitize_filename(group) + f"/{oll}_{name}"
        if os.path.exists(oll_path):
            shutil.rmtree(oll_path)
        os.makedirs(oll_path)
        f.write(f"curl \"http://192.168.122.154/visualcube/visualcube.php?fmt=svg&case={alg}&view=plan&size=1024&stage=oll&bg=t\" > \"{sanitize_filename(group)}/{oll}_{name}.svg\"\n")
        for i in range(0, repeat + 1):
            f.write(f"curl \"http://192.168.122.154/visualcube/visualcube.php?fmt=svg&alg={alg*i}&view=plan&size=1024&stage=ll&bg=t\" > \"orders/{sanitize_filename(group)}/{oll}_{name}/power_{i}.svg\"\n")
