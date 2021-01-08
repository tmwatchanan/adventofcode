def part1(locations):
    trees = 0
    row = 1
    col = 3
    n_cols = len(locations[0])
    print("n_cols", n_cols)
    while row < len(locations):
        point = locations[row][col % n_cols]
        if point == '#':
            trees += 1
        
        row += 1
        col += 3
        
    return trees

def part2(locations):
    trees = 0
    return trees
        

locations = open("input").read().strip().split("\n")
print(locations)
print(part1(locations))
#print(part2(locations))

