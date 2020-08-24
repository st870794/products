products = []
while True:
	name = input('請輸入商品名稱(結束:q): ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])
print(products)# 大清單

# print(products[0][1])
# 大清單第0格中的小清單第0格

for p in products:# 逐一列出小清單
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w',encoding = 'utf-8') as f: # w:寫入模式,csv:計資料更好用的檔案
	f.write('商品,價格\n') # 寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 開始寫入的動作