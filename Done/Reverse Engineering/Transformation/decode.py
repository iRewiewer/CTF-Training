flag = open("enc", "rb").read().decode()

for i in flag:
	print(bytes.fromhex(hex(ord(i)).lstrip("0x")).decode("ASCII"), end = "")