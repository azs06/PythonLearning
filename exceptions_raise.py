class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')


print("Always write beautiful code!")

#print('that's cool')

print('''
Did that stop the old Grinch?
No! The Grinch simply said,
"If I can't find a reindeer,
I'll make one instead!"
''')

print('''
"""
THIS IS A STRING
"""
''')

