## 找尋基礎檔案並讀取大清單出來

import os # operating system
products = []
if os.path.isfile('products.csv'): # os作業系統, path路徑模組, isfile檢查檔案
	print('找到原始檔案')
	with open('products.csv', 'r')as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過if的條件一迴後，後繼續11.12行(簡單說就是跳到下一迴)
			name, price = line.strip().split(',') # strip去除換行符號(\n) 
			products.append([name, price]) # 把分成2份的小清單加入大清單products中
	# 因為表單中有分商品及價格，所以第11行是把變數命名成name, price
	# 並且是讓split幫我分成兩份清單，若是要分成3份清單或以上，要有相對數量的變數命名
	print(products)
else:
	print('尚未建立基礎檔案...')


## 讓使用者輸入及編寫新清單

while True:
	name = input('請輸入商品名稱(結束:q): ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price]) # 建立新的小清單name跟price
print(products) # products是大清單

# print(products[0][1])
# 大清單第0格中的小清單第0格

for p in products:# 逐一列出小清單
	print(p[0], '的價格是', p[1])

## 將新清單寫入檔案中

with open('products.csv', 'w',) as f: # w:寫入模式,csv:計資料更好用的檔案
	f.write('商品,價格\n') # 寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 開始寫入的動作


