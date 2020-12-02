import re

re_object = re.compile(r"(\d+)-(\d+) (\S): (\S+)")
valid_passwords = 0
with open('input') as f:
    for line in f:
        match = re_object.match(line)
        current_matches = 0
        if len(match.group(4)) >= int(match.group(1)) and match.group(4)[int(match.group(1)) - 1] == match.group(3):
            current_matches += 1
        if len(match.group(4)) >= int(match.group(2)) and match.group(4)[int(match.group(2)) - 1] == match.group(3):
            current_matches += 1
        valid_passwords += current_matches % 2

    print(valid_passwords)
