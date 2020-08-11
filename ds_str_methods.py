name = 'Swaroop'

if name.startswith('S'):
    print('Yes, starts with S')

if 'a' in name:
    print('Yes it contains string "a"')

if name.find('war') != -1:
    print('Yes it contains string "war"')

delimeter = "_*_"
mylist = ['apple', 'orange', 'pineapple']
print(delimeter.join(mylist))
