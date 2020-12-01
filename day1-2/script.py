with open('input') as f:
    input_lines = [int(line.rstrip()) for line in f]
for input in input_lines:
    for input2 in input_lines:
        if 2020 - input - input2 in input_lines:
            print(input * input2 * (2020 - input - input2))
            exit()
