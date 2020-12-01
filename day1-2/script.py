input_lines = []
with open('input') as f:
    for line in f:
        if line.strip():
            input_lines.append(int(line.strip()))

done = False
for input in input_lines:
    if done:
        break
    for input2 in input_lines:
        if 2020 - input - input2 in input_lines:
            print(input * input2 * (2020 - input - input2))
            done = True
            break
