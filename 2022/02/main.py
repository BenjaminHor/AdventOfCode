file = open("input.txt", "r")
lines = file.readlines()

my_score = 0

# x lose, y draw, z win
map = {"X": 1, "Y": 2, "Z": 3}
for line in lines:
    other = line[0]
    mine = line[2]
    if other == "A" and mine == "Y":
        my_score += 6
    elif other == "B" and mine == "Z":
        my_score += 6
    elif other == "C" and mine == "X":
        my_score += 6
    elif (
        (other == "A" and mine == "X")
        or (other == "B" and mine == "Y")
        or (other == "C" and mine == "Z")
    ):
        my_score += 3

    my_score += map[mine]

print(my_score)

my_score = 0
for line in lines:
    other = line[0]
    mine = line[2]

    if mine == "X":
        if other == "A":
            my_score += map["Z"]
        elif other == "B":
            my_score += map["X"]
        elif other == "C":
            my_score += map["Y"]
    elif mine == "Y":
        if other == "A":
            my_score += map["X"]
        elif other == "B":
            my_score += map["Y"]
        elif other == "C":
            my_score += map["Z"]
        my_score += 3
    elif mine == "Z":
        if other == "A":
            my_score += map["Y"]
        elif other == "B":
            my_score += map["Z"]
        elif other == "C":
            my_score += map["X"]
        my_score += 6

print(my_score)
