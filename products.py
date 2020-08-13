products = []
while True:
	name = input('請輸入商品名稱(結束:q): ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)# 大清單

# print(products[0][1])
# 大清單第0格中的小清單第0格

for p in products:# 逐一列出小清單
	print(p[0], '的價格是', p[1])