price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

price-=bonus if bonus_granted else price
print(price)