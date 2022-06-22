file = [int(i) for i in open("message.txt", 'r').read().split(' ')[:-1]]

print("picoCTF{", end = "")

digits = [0,1,2,3,4,5,6,7,8,9]
alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in file:
    i = int(i) % 37
    if i == 36: print("_", end = "")
    elif i >= 26 and i <= 35: print(digits[i%26], end = "")
    elif i >= 0 and i <= 25: print(alphabet[i], end = "")

print("}", end = "")