
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100 == 0:
			print(count)
	
print(data[0])
		




