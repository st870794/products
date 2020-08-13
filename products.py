products = []
while True:
	name = input('請輸入商品名稱(結束:q): ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

# print(products[0][1])
# 大清單第0格中的小清單第0格