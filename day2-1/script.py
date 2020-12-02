import re

re_object = re.compile(r"(\d+)-(\d+) (\S): (\S+)")
valid_passwords = 0
with open('input') as f:
    for line in f:
        match = re_object.match(line)
        if match.group(4).count(match.group(3)) >= int(match.group(1)) and \
           match.group(4).count(match.group(3)) <= int(match.group(2)):
            valid_passwords += 1

print(valid_passwords)
