fields_required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
fields_left = fields_required[:]
valid_passports = 0
with open('input') as f:
    for line in f:
        if line.strip() == '':
            if not len(fields_left):
                valid_passports += 1
            fields_left = fields_required[:]
        for field in line.split():
            if field[0:3] in fields_left:
                fields_left.remove(field[0:3])
if not len(fields_left):
    valid_passports += 1
print(valid_passports)
