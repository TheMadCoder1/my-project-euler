def char_sum(name):
    return sum([ord(char) - ord('A') + 1 for char in name])


with open("names.txt", "r") as f:
    names = [n[1:-1] for n in f.read().split(",")]

names.sort()
total = 0
for i in range(len(names)):
    total += (i+1) * char_sum(names[i])

print(total)