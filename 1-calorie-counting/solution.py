current = 0
highest = [0, 0, 0]
with open('data.txt') as file:
    for line in file:
        line = line.replace("\n", "")
        if line:
            current += int(line)
        else:
            if current > highest[0]:
                highest[0] = current
                highest = sorted(highest)
            current = 0
if current > highest[0]:
    highest[0] = current
    highest = sorted(highest)
print(sum(highest))
