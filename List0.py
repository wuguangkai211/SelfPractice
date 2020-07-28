
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banan']
print("Now ID is:", id(shoplist))

#对此 List （可变数据类型）重新赋值，地址发生改变
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("Now ID is:", id(shoplist))

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end = ' ')
for item in shoplist:
    print(item, end = ' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

#修改（例如append、+=，与赋值 `=` 区分）此 List （可变数据类型），地址不变
print("Now ID is:", id(shoplist))

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
