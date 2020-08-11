age = 20
name = "Soikat"
print("{0} was {1} when it was 2008".format(name, age))
print(f'{name} was {age} when it was 2008')

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))

print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

escape_single_quote = 'What \'s your name'
escape_double_quote = "What\"s your name"
print(escape_single_quote)
print(escape_double_quote)

raw_string = r"Newlines are indicated by \n"
print(raw_string)
s = 'This is a string. \
This continues the string.'
print(s)
