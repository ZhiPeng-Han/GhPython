width = input('Please enter width: ')

price_width = 10
item_width = width - price_width

head_format = '%-*s%*s'
formayt = '%-*s%*.2f'

print '=' * width

print head_format % (item_width,'Item',price_width,'Price')

print '-' * width

print formayt % (item_width,'Apples',price_width,0.4)
print formayt % (item_width,'Prunes(4 lbs)',price_width,12)

print '=' * width
