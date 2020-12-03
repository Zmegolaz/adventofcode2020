trees, linenum = 1, 0
paths = [{'trees': 0, 'position': 0, 'path': (1, 1)}, {'trees': 0, 'position': 0, 'path': (3, 1)}, {'trees': 0, 'position': 0, 'path': (5, 1)}, {'trees': 0, 'position': 0, 'path': (7, 1)}, {'trees': 0, 'position': 0, 'path': (1, 2)}]
with open('input') as f:
    length = len(f.readline().strip())
    f.seek(0)
    for line in f:
        for path in paths:
            if not linenum % path['path'][1]:
                if line[path['position'] % length] == '#': path['trees'] += 1
                path['position'] += path['path'][0]
        linenum += 1
for path in paths:
    trees *= path['trees']
print(trees)
