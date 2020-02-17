# 寫程式碼讀取留言檔(reviews.txt)
# 測試印出data清單
# 只印出第0筆看看
# 印出data長度，順便算讀取進度
# bonus：每1000次才印出進度
# 算留言平均長度(多少字)
# 清單篩選：找出多少留言是小於100個字以內的
# 清單篩選：把留言有提到good這個字的取出來


# 印出總資料筆數，每1000筆顯示出資料讀取進度
data =[]
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 1000 == 0:
			print(len(data))
	print(data[0])
	print('檔案讀取完了，總共有', len(data), '筆資料')

# 算出留言平均長度
sum_len = 0
for num_str in data:
	sum_len += len(num_str)
print('平均的留言長度有', sum_len/len(data), '個字')

# 清單篩選：找出多少留言是小於100個字以內的
# 順便把這小於100字的留言整理出來
new_data = []
count_100 = 0
for d in data:
	if len(d) < 100:
		new_data.append(d.strip())
		count_100 += 1
print('一共有', count_100, '則留言小於100字')
print(new_data[0])

# 清單篩選：把留言有提到good/Good這個字的取出來
good_data = []
for d in data:
	if 'good' in d:
		good_data.append(d)
	elif 'Good' in d:
		good_data.append(d)
print(good_data[0])
print('一共有', len(good_data), '筆留言提到good/Good')

