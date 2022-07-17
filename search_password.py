searched_site = input('Password for site: ')

file = open('passwords.txt', 'r')


for index, line in enumerate(file):
    if searched_site in line:
        print(line)
else:
    print('No match found')