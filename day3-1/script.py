trees, position = 0, 0
with open('input') as f:
    length = len(f.readline().strip())
    for line in f:
        position += 3
        if line[position % length] == '#': trees += 1 
print(trees)
