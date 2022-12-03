result = 0
def process(input_file):
    side1 = set(next(input_file).replace('\n', ''))
    side2 = set(next(input_file).replace('\n', ''))
    side3 = set(next(input_file).replace('\n', ''))
    print(side1, side2, side3)
    result = [c for c in side1 if c in side2 and c in side3]
    print(result)
    return result[0], input_file

def score(c):
    if c.isupper():
        return ord(c) - ord("A") + 27
    else:
        return ord(c) - ord('a') + 1

with open('data.txt') as input_file:
    for i in range(100):
        char, input_file = process(input_file)
        result += score(char)

print(result)