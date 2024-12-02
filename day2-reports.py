success = 0
with open("data2.txt") as file:
    for line in file:
        line = line.replace("\n","").split()
        up = 1
        down = 1
        fail = 0
        i = 1
        while (i < len(line)):
            if int(line[i-1]) - int(line[i]) >= 0:
              down = 0
            if int(line[i-1]) - int(line[i]) <= 0:
              up = 0
            if abs(int(line[i-1]) - int(line[i])) > 3:
              fail = 1
            i = i + 1
        if (up == 1 or down == 1) and fail == 0:
          success = success + 1
          #print(line)
print(success)

# Problem Dampener Logic
success = 0
with open("data2.txt") as file:
    for line in file:
        line = line.replace("\n","").split()
        up = 1
        down = 1
        fail = 0
        i = 1
        while (i < len(line)):
            if int(line[i-1]) - int(line[i]) >= 0:
              down = 0
            if int(line[i-1]) - int(line[i]) <= 0:
              up = 0
            if abs(int(line[i-1]) - int(line[i])) > 3:
              fail = 1
            i = i + 1
        if (up == 1 or down == 1) and fail == 0:
          success = success + 1
        else:
            j = 0
            while j < len(line):
                newline = line[:j] + line[j+1:]
                newup = 1
                newdown = 1
                newfail = 0
                #print(newline)
                i = 1
                while (i < len(newline)):
                    if int(newline[i-1]) - int(newline[i]) >= 0:
                        newdown = 0
                    if int(newline[i-1]) - int(newline[i]) <= 0:
                        newup = 0
                    if abs(int(newline[i-1]) - int(newline[i])) > 3:
                        newfail = 1
                    i = i + 1
                if (newup == 1 or newdown == 1) and newfail == 0:
                    success = success + 1
                    print(line)
                    j = len(line)
                j = j + 1
print(success)