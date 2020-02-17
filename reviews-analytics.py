# 寫程式碼讀取留言檔(reviews.txt)
# 測試印出data清單
# 只印出第0筆看看
# 印出data長度，順便算讀取進度
# bonus：每1000次才印出進度
# 算留言平均長度(多少字)
# 

data =[]
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 1000 == 0:
			print(len(data))
	print(data[0])
	print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for num_str in data:
	sum_len += len(num_str)
print('平均的留言長度有', sum_len/len(data), '個字')


		




