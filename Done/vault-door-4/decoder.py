asciiv = [106, 85, 53, 116, 95, 52, 95, 98]
hexv = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
idkv = [0o0142, 0o0131, 0o0164, 0o063 , 0o0163, 0o0137, 0o0143, 0o061]
strv = ['9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e']

for i in asciiv + hexv + idkv:
	print(chr(i), end="")

for i in strv:
	print(i, end="")