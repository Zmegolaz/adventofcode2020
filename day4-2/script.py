import re

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
            if re.match(r'byr:(19[2-9]\d|200[0-2])$', field) or \
               re.match(r'iyr:(201\d|2020)$', field) or \
               re.match(r'eyr:(202\d|2030)$', field) or \
               re.match(r'hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$', field) or \
               re.match(r'hcl:#[0-9a-f]{6}$', field) or \
               re.match(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)$', field) or \
               re.match(r'pid:\d{9}$', field):
                fields_left.remove(field[0:3])
if not len(fields_left):
    valid_passports += 1
print(valid_passports)
