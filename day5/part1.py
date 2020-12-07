highest_seat = 0
with open('input') as f:
    for line in f:
        highest_seat = max(highest_seat, int(line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2))
print(highest_seat)
