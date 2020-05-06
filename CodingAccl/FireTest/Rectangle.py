with open(chemin_1, "r") as f1:
    c1 = f1.read().split()

with open(chemin_2, "r") as f2:
    c2 = f2.read().split()

def rectangle(c1, c2):
    target = c1
    grid = c2
    position = 0

    for i in range(len(grid) - len(target) + 1):
        if target[0] in grid[i]:
            position = grid[i].index(target[0])

        if target[1] in grid[i + 1] and grid[i + 1].index(target[1]) == position:
            if target[2] in grid [i + 2] and grid[i + 2].index(target[2]) == position:
                return position, i
        
    return False


print(rectangle(c1, c2))
