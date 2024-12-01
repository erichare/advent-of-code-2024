## PUZZLE 1
# PART 1

# Read in the input1 file
with open('input1.txt') as f:
    lines = f.readlines()

# Make lists of each column and convert to integer
col1 = sorted([int(x.split()[0]) for x in lines])
col2 = sorted([int(x.split()[1]) for x in lines])

# Compute the differences between col1 and col2 (absolute)
diff = [abs(x-y) for x,y in zip(col1, col2)]

# Sum up the differences
puzzle1_solution1 = sum(diff)
print(puzzle1_solution1)

# PART 2
# For each number in col1, multiply by number of appearances in col2

# Create a dictionary of col2
col2_dict: dict[int, int] = {}
for i in col2:
    if i in col2_dict:
        col2_dict[i] += 1
    else:
        col2_dict[i] = 1

# Multiply each number in col1 by the number of appearances in col2
puzzle1_solution2 = 0

for i in col1:
    if i in col2_dict:
        puzzle1_solution2 += i * col2_dict[i]

print(puzzle1_solution2)
