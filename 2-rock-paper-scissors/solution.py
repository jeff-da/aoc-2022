def evaluate(a, b):
    a_val = ord(a) - ord("A")
    b_val = ord(b) - ord("X")
    if b == "Y":
        return a_val + 1
    if b == "Z":
        return a_val + 2 if a_val < 2 else 1
    if b == "X":
        return a_val if a_val != 0 else 3

def score(line):
    a = line.split()[0]
    b = line.split()[1]
    result = (ord(b) - ord("X")) * 3
    result += evaluate(a, b)
    return result

result = 0
with open('data.txt') as file:
    for line in file:
        line = line.strip()
        result += score(line)
print(result)