string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

group_of_numbers = 10

my_list = '.'.join([
    string[index:index + group_of_numbers]
    for index in range(0, len(string), group_of_numbers)
])

print(my_list)