ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.com',
    'Matsumoto': 'matz@ruby-lang.com',
    'Spammer': 'Spammer@hotmail.com'
}

print('Swaroop\'s address is', ab['Swaroop'])

del ab['Spammer']

print('\n There are {} contacts in the address book\n'.format(len(ab)))

for name, address in ab.items():
    print(name, address)
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nGuido\'s address', ab['Guido'])
