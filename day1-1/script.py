with open('input') as f:
    input_lines = [line.rstrip() for line in f]

for input in input_lines:
    if str(2020 - int(input)) in input_lines:
        print(int(input) * (2020 - int(input)))
        break
