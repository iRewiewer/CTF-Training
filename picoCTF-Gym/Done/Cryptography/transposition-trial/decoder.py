file = open("message.txt", "r")

count = 0
message = []
block = []

for i in file.read():
	block.append(i)
	count += 1
	
	if(count == 3):
		count = 0
		message.append(block)
		block = []

for i in message:
	print(i[2] + i[0] + i[1], end = "")