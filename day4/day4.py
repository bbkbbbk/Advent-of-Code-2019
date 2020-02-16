import re


def check_increasing(data):
    return all(i <= j for i, j in zip(data, data[1:]))


def check_double(data):
    return any(i == j for i, j in zip(data, data[1:]))


def check_exactly_double(data):
    matcher = re.compile(r'(.)\1*')
    repeated_number = [match.group() for match in matcher.finditer(data)]
    return any(len(i) == 2 for i in repeated_number)


raw_data = '246515-739105'
low, high = map(int, raw_data.split('-'))
num_passwords_1 = num_passwords_2 = 0

for i in range(low, high + 1):
    str_i = str(i)
    if check_increasing(str_i):
        if check_double(str_i):
            num_passwords_1 += 1
        if check_exactly_double(str_i):
            num_passwords_2 += 1

print('How many different passwords:', num_passwords_1)
print('How many different passwords:', num_passwords_2)
