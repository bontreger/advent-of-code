with open('data4.txt', 'r') as file:
  space = [ ]
  for line in file.read().splitlines():
    space.append(line)

#print(space)
ymax = len(space[0])-1
xmax = len(space)-1

#find an X
x = 0
matches = 0
while x <= xmax:
    #print("row",x)
    y = 0
    while y <= ymax:
        #print("column",y)
        if space[x][y] == "X":
        # if we found an X, check every direction for an M
            # West
            if x > 2 and space[x-1][y] == "M":
                if space[x-2][y] == "A":
                    if space[x-3][y] == "S":
                        matches = matches + 1
            # Northwest
            if x > 2 and y > 2 and space[x-1][y-1] == "M":
                if space[x-2][y-2] == "A":
                    if space[x-3][y-3] == "S":
                        matches = matches + 1
            # North
            if y > 2 and space[x][y-1] == "M":
                if space[x][y-2] == "A":
                    if space[x][y-3] == "S":
                        matches = matches + 1
            # Northeast
            if y > 2 and x < xmax - 2 and space[x+1][y-1] == "M":
                if space[x+2][y-2] == "A":
                    if space[x+3][y-3] == "S":
                        matches = matches + 1
            # East
            if x < xmax - 2 and space[x+1][y] == "M":
                if space[x+2][y] == "A":
                    if space[x+3][y] == "S":
                        matches = matches + 1
            # Southeast
            if x < xmax - 2 and y < ymax - 2 and space[x+1][y+1] == "M":
                if space[x+2][y+2] == "A":
                    if space[x+3][y+3] == "S":
                        matches = matches + 1
            # South
            if y < ymax - 2 and space[x][y+1] == "M":
                if space[x][y+2] == "A":
                    if space[x][y+3] == "S":
                        matches = matches + 1
            # Southwest
            if y < ymax - 2 and x > 2 and space[x-1][y+1] == "M":
                if space[x-2][y+2] == "A":
                    if space[x-3][y+3] == "S":
                        matches = matches + 1
        y = y + 1
    x = x + 1

print(matches)

# finx an X of mas.... who thinks of this
# find an A
# check that M and S are on opposite corners
# Ignore column 0 and max so we can avoid indexing issues
matches2 = 0
x = 1
while x <= xmax-1:
    y = 1
    while y <= ymax-1:
        if space[x][y] == "A":
        #brute force check for the MAS pattern options
            if space[x-1][y-1] == "M" and space[x+1][y+1] == "S":
                if space[x-1][y+1] == "M" and space[x+1][y-1] == "S":
                    matches2 = matches2 + 1
                if space[x+1][y-1] == "M" and space[x-1][y+1] == "S":
                    matches2 = matches2 + 1
            if space[x+1][y+1] == "M" and space[x-1][y-1] == "S":
                if space[x-1][y+1] == "M" and space[x+1][y-1] == "S":
                    matches2 = matches2 + 1
                if space[x+1][y-1] == "M" and space[x-1][y+1] == "S":
                    matches2 = matches2 + 1
        y = y + 1
    x = x + 1
print(matches2)