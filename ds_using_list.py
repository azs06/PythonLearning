shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')

for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice')

shoplist.append('rice')
print('My shopping list is now:', shoplist)

print('I will sort my list')
shoplist.sort()
print('Shored shopping list is', shoplist)

print('The first item to buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]

print('I bought the old item', olditem)
print('My shopping list is:', shoplist)
