seats_possible, seats_taken = set(), set()
with open('input') as f:
    for line in f:
        seat = int(line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
        seats_taken.add(seat)
        if seat in seats_possible:
            seats_possible.remove(seat)
        if seat - 1 not in seats_taken:
            seats_possible.add(seat - 1)
        if seat + 1 not in seats_taken:
            seats_possible.add(seat + 1)
seats_possible.remove(min(seats_possible))
print(min(seats_possible))
