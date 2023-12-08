print("Day 1 - Trebuchet")

# Using readlines()
# file = open("input.data", "r")
file = open("example.data", "r")
lines = file.readlines()

# read lines
for line in lines:
    print(line)
    for i in range(len(line)):
        c = line[i]
        if c.isnumeric():
            print(c)
            break
