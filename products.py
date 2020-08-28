import os # operating system

#讀取大清單出來
def read_file(filename):
	products = []
	with open(filename, 'r')as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過if的條件一迴後，後繼續11.12行(簡單說就是跳到下一迴)
			name, price = line.strip().split(',') # strip去除換行符號(\n) 
			products.append([name, price]) # 把分成2份的小清單加入大清單products中
		# 因為表單中有分商品及價格，所以第11行是把變數命名成name, price
		# 並且是讓split(用逗點當切割標準)幫我分成兩份清單，若是要分成3份清單或以上，要有相對數量的變數命名
	return products # 定義動作跑完都要回傳更新

## 讓使用者輸入及編寫新清單
def user_imput(products):
	while True:
		name = input('請輸入商品名稱(結束:q): ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price]) # 建立新的小清單name跟price
	print(products) # products是大清單
	return products # 定義動作跑完都要回傳更新

	# print(products[0][1])
	# 大清單第0格中的小清單第0格

## 印出購買紀錄
def print_products(products):
	for p in products:# 逐一列出小清單
		print(p[0], '的價格是', p[1])

## 將新清單寫入檔案中
def write_file(filename, products):
	with open(filename, 'w') as f: # w:寫入模式,csv:計資料更好用的檔案
		f.write('商品,價格\n') # 寫入欄位名稱
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') # 開始寫入的動作

## 找尋原始檔案(主要定義)
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # os作業系統, path路徑模組, isfile檢查檔案
		print('找到原始檔案')
		products = read_file(filename) # 把第一個定義的參數外移，這樣就可以投入不同檔案
	else:
		print('尚未建立基礎檔案...')

	products = user_imput(products)
	print_products(products)
	write_file('products.csv', products)

main()
