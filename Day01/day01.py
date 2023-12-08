print("Day 1 - Trebuchet")

# Using readlines()
# file = open("input.data", "r")
file = open("example.data", "r")
lines = file.readlines()

# read lines
for line in lines:
    print(line)
    d0 = "0"
    d1 = "0"
    # ---
    for i in range(len(line)):
        c = line[i]
        if c.isnumeric():
            d0 = int(c)
            # print(int(c))
            break
    # ---
    for index in reversed(range(len(line))):
        character = line[index]
        # --- check if it is a numeric
        if character.isnumeric():
            # print(c)
            d1 = int(character)
            # --- we do not need to got further
            break
    # ---
    print(d0)
    print(d1)
    number = d0 * 10 + d1
    # number = "d0" + "d1"
    print(number)
