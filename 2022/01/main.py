file = open("input.txt", "r")
lines = file.readlines()

calories = []
max_sum = 0
curr_sum = 0
for line in lines:
    if line == "\n":
        max_sum = max(max_sum, curr_sum)
        calories.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(line)

calories.sort()

print(calories[-1])
print(calories[-1] + calories[-2] + calories[-3])
