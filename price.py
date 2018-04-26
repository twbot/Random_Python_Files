price = 24.95
disc = .4
ship_cost = 0
shipping = int(input('Please enter desired number of books: '))
if shipping > 1:
	ship_cost = 3.0 + (.75*((shipping)-1))
else:
	ship_cost = 3.0
price_book = price - (price*disc)
price = shipping*(price_book)+ship_cost
print(round(price, 5))
